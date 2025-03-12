from dataclasses import dataclass



class UDPPacket:
    def __init__(self,data,sequence_number):
        self.data = data
        self.sequence_number = sequence_number



    def __str__(self):
        return f'data is {self.data} and ack number is {self.sequence_number}'