# User Datagram Protocol (UDP)

> Vidath Dissanayake | Sri Lanka

UDP is not considered as a reliable protocol as it is a connectionless protocol. We do not get conformation whether the packet was received. However, the speed of the data transfer is higher than a connection oriented protocol such as [TCP](TCP.md), as there is no waiting for conformation. The header of UDP is also much smaller, and there is much less overhead when using UDP than [TCP](TCP.md).

Therefore, UDP is used in situations where reliability is not as important as speed as well as in instances where retransmission is not preferable For example,
- VoIP calls


## UDP Header

Below is a visual representation of the UDP header.

![udp header](assets/images/udp%20header.png)

- [Source Port](#Source%20Port): A 16-bit field that identifies the port initiating the connection.
- [Destination Port](#Destination%20Port): A 16-bit field that identifies the port receiving the connection.
- [Length](#Length):
- [Checksum](#Checksum): A 16-bit field used for error checking both the header and the payload of the segment.

### Source Port

### Destination Port

### Length

### Checksum