import pickle
import socket
from types import new_class

from UDPPacket import UDPPacket

class rdt_sender:
    sequence_number = 0
    def __init__(self,UDP_IP,UDP_PORT):
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.UDP_CONNECTION = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self.is_bind = False

    def rdt_send(self,data):
        print(data)

        self.udt_send(self.make_packet(data))

    def udt_send(self,data):
        byte_data = pickle.dumps(data)
        self.UDP_CONNECTION.sendto(byte_data,(self.UDP_IP,self.UDP_PORT))

    def rdt_rcv(self):
        data,addr = self.UDP_CONNECTION.recvfrom(1024)
        new_data = pickle.loads(data)
        if self.deliver_data(new_data) == 'ACK':
            self.sequence_number = (self.sequence_number+1) %2
            return self.deliver_data(new_data)
        else:
            pass
        #new_data = pickle.loads(data)
        # if self.is_ack(new_data):
        #     print("acknowledged")
        #     self.expected_ack_number = (self.expected_ack_number+1)%2
        #     return self.deliver_data(new_data), addr
        # else:
        #     pass

    def deliver_data(self,packet: UDPPacket):
        return packet.data

    def make_packet(self,data):
        return UDPPacket(data,self.sequence_number)

    def is_ack(self,packet:UDPPacket):
        pass

    def start_timer(self):
        pass

    def stop_timer(self):
        pass


