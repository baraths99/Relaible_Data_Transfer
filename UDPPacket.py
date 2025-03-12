

class UDPPacket:

    def __init__(self, ack_number:int, seq_number:int):
        self.ack_number = ack_number
        self.seq_number = seq_number
