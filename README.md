# Reliable Data Transfer Protocol Implementation

This project implements a reliable data transfer protocol over UDP connections, effectively simulating TCP-like reliability. The implementation follows the RDT 3.0 model which provides reliability through sequence numbers, acknowledgments, timeouts, and checksum-based error detection.

## Overview

UDP is a connectionless, unreliable transport protocol that doesn't guarantee packet delivery, order, or protection against duplication. This project builds a reliability layer on top of UDP to ensure:

- Guaranteed message delivery
- Message integrity
- Proper sequencing
- Flow control
- Congestion control

## Features

- **Stop-and-Wait Protocol**: Implementation of the basic RDT 3.0 model
- **Checksum-based Error Detection**: Ensures data integrity during transmission
- **Timeout and Retransmission**: Handles packet loss in the network
- **Sequence Numbers**: Manages proper ordering of packets
- **Acknowledgment System**: Confirms successful packet reception

## Implementation Details

The project uses Python and raw sockets to implement the RDT protocol. It consists of:

1. A sender that wraps messages in protocol-specific headers
2. A receiver that processes incoming packets and sends acknowledgments
3. Timeout handling to detect lost packets
4. Sequence number management to detect duplicates and maintain order


## TODO List

- [ ] Implement Go-Back-N protocol for improved efficiency
- [ ] Add Three-Way Handshake for connection establishment
- [ ] Implement congestion control algorithms
