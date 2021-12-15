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