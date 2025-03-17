import pickle
import socket
import time
import threading

from UDPPacket import UDPPacket

class rdt_sender:
    sequence_number = 0
    def __init__(self,UDP_IP,UDP_PORT,timeout=1.0):
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.UDP_CONNECTION = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.sequence_number = 0
        self.timeout = timeout
        self.timer = None
        self.current_packet = None
        self.waiting_for_ack = False


    def rdt_send(self,data):
        self.current_packet = self.make_packet(data)
        self.udt_send(self.current_packet)
        self.waiting_for_ack = True
        self.start_timer()

        while self.waiting_for_ack:
            try:
                ack = self.rdt_rcv()
                if ack == 'ACK' and not self.is_corrupt():
                    self.stop_timer()
                    self.sequence_number = (self.sequence_number + 1) % 2
                    self.waiting_for_ack = False
            except socket.timeout:
                pass

    def udt_send(self,data):
        byte_data = pickle.dumps(data)
        self.UDP_CONNECTION.sendto(byte_data,(self.UDP_IP,self.UDP_PORT))
        print(f"Sent packet: {data}")

    def rdt_rcv(self):
        data,addr = self.UDP_CONNECTION.recvfrom(1024)
        new_data = pickle.loads(data)
        print(f"Received: {new_data}")
        if new_data.is_ack and new_data.sequence_number == self.sequence_number:
            return self.deliver_data(new_data)
        else:
            print(f"Received wrong ACK: expected {self.sequence_number}, got {new_data.sequence_number}")
            return None

    def deliver_data(self,packet: UDPPacket):
        return packet.data

    def make_packet(self,data):
        return UDPPacket(data,self.sequence_number)

    def is_ack(self,packet:UDPPacket):
        pass

    def start_timer(self):
        self.stop_timer()
        self.timer = threading.Timer(self.timeout,self.timeout_handler)

    def stop_timer(self):
        if self.timer:
            self.timer.cancel()
            self.timer = None

    def timeout_handler(self):
        print("Timeout occurred, retransmitting...")
        if self.waiting_for_ack and self.current_packet:
            self.udt_send(self.current_packet)
            self.start_timer()

    def is_corrupt(self, packet):
        return packet.is_corrupt() if hasattr(packet, 'is_corrupt') else False
