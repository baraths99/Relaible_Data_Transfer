
class UDPPacket:
    def __init__(self, data, sequence_number, checksum=None, is_ack=False):
        self.data = data
        self.sequence_number = sequence_number
        self.is_ack = is_ack
        self.checksum = checksum if checksum else self.calculate_checksum()

    def calculate_checksum(self):
        if isinstance(self.data, str):
            return sum(ord(c) for c in self.data) % 256
        return 0

    def is_corrupt(self):
        return self.checksum != self.calculate_checksum()

    def __str__(self):
        packet_type = "ACK" if self.is_ack else "DATA"
        return f'{packet_type} packet, seq={self.sequence_number}, data={self.data}, checksum={self.checksum}'