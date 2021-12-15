# Transmission Control Protocol (TCP)

> Created: Vidath Dissanayake | 2021/12/15 | Sri Lanka

TCP is a reliable protocol or a connection oriented protocol as it sets up a connection between the two devices that are communicating and acknowledges receiving of packets and retransmits dropped packets to prevent the data from being corrupted.

[TCP 3-Way Handshake](#TCP%203-Way%20Handshake) is used to establish the TCP connection between the two communicating devices. Then, [TCP Information Communication](#TCP%20Information%20Communication) is done using the connection.

## TCP 3-Way Handshake

Here a few messages are exchanged.

- SYN (Synchronization)
- ACK (Acknowledgement)

The handshake goes as follows.

1. The client sends a SYN message to the server.
2. The server sends a SYN-ACK message to the client.
3. The client sends an ACK message to a server.

Then the handshake is complete, and the connection is established.


## TCP Information Communication

Each time the information is sent, the following happens. Let's assume that the client is sending information to the server.
1. The client sends segment 1 to the server.
2. The server sends ACK 2 saying it is ready to receive segment 2.
3. The client doubles the number of segments (window size).
4. The server sends ACK n, where n is the next packet it is expecting. If a segment was dropped, it will send the number of the segment that was dropped.
5. If n is a segment that the client already transmitted, it will reduce the window size and transmit again. If not, the client will double the windows size until a packet is dropped.


## TCP Header

Below is a visual representation of the TCP header.

![tcp header](assets/images/tcp%20header.png)

- Source Port: A 16-bit field that identifies the port initiating the connection.
- Destination Port: A 16-bit field that identifies the port receiving the connection.
- Sequence Number: A 32-bit field that specifies the first sequence number if the SYN flag = 1 or the accumulated sequence number if the SYN flag = 0.
- Acknowledgement Number: A 32-bit field that specifies the next sequence number the sender of an ACK expects (if ACK flag = 1).
- Data Offset: A 4-bit field that specifies the size of the TCP header, with a unit measure of 32-bit words (the minimum value is 5 and the maximum value is 15).
- Reserved: A 3-bit field reserved for future use, where each bit is set to a value of 0.
- Flags: A series of nine 1-bit fields, each representing a different TCP flag (e.g. The SYN, ACK and URG flags).
- Window Size: A 16-bit field indicating the number of bytes the sender of the segment is willing to receive.
- Checksum: A 16-bit field used for error checking both the header and the payload of the segment.
- Urgent Pointer: A 16-bit field indicating the last urgent data byte (if URG flag = 1).
- Options: A field whose size is in the range of 0-320 bits and can be used to indicate a variety of additional TCP options.