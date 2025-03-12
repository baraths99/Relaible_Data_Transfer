import pickle
import socket

from UDPPacket import UDPPacket


class rdt_receiver:
    expected_sequence_number = 0
    def __init__(self, UDP_IP, UDP_PORT):
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.UDP_CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDP_CONNECTION.bind((self.UDP_IP, self.UDP_PORT))

    def rdt_send(self):
        return self.make_packet()

    def udt_send(self,address):
        send_packet = self.make_packet()
        send_packet = pickle.dumps(send_packet)
        self.UDP_CONNECTION.sendto(send_packet, (address[0], address[1]))

    def rdt_rcv(self):
        data, addr = self.UDP_CONNECTION.recvfrom(1024)
        new_data = pickle.loads(data)
        if self.has_seq0(new_data):
            self.udt_send(addr)
            self.expected_sequence_number = (self.expected_sequence_number+1) % 2
            return self.extract_data(new_data), addr
        else:
            pass

    def has_seq0(self,packet: UDPPacket):
        return self.expected_sequence_number == packet.sequence_number


    def extract(self):
        pass

    def extract_data(self,packet: UDPPacket):
        return packet.data

    def make_packet(self):
        return UDPPacket("ACK",self.expected_sequence_number)