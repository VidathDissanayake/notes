# Transmission Control Protocol (TCP)

> Vidath Dissanayake | Sri Lanka

TCP is a reliable protocol or a connection oriented protocol as it sets up a connection between the two devices that are communicating and acknowledges receiving of packets and retransmits dropped packets to prevent the data from being corrupted.

[TCP 3-Way Handshake](#TCP%203-Way%20Handshake) is used to establish the TCP connection between the two communicating devices. Then, [TCP Information Communication](#TCP%20Information%20Communication) is done using the connection.

## TCP 3-Way Handshake

Here a few messages are exchanged.

- [[#SYN]] (Synchronization)
- [[#ACK]] (Acknowledgement)

The handshake goes as follows.

1. The client sends a [[#SYN]] message to the server.
2. The server sends a [[#SYN]]-[[#ACK]] message to the client.
3. The client sends an [[#ACK]] message to a server.

Then the handshake is complete, and the connection is established.


## TCP Information Communication

Each time the information is sent, the following happens. Let's assume that the client is sending information to the server.
1. The client sends segment 1 to the server.
2. The server sends [[#ACK]] 2 saying it is ready to receive segment 2.
3. The client doubles the number of segments (window size).
4. The server sends an [[#ACK]], with the sequence number of the next segment that it expects, base on the last segment received in sequence. If a segment was dropped, it can be identified because of this.
5. If the [[#ACK]] number received by the client is a segment that the client already transmitted, it will reduce the window size and transmit again. If not, the client will double the windows size until a [packet](../../../reference%20models/OSI%20Model/PDU/packet.md) is dropped.


## TCP Header

Below is a visual representation of the TCP [header](../../structure%20of%20a%20protocol/header.md).

![tcp header](assets/images/tcp%20header.png)

- [Source Port](#Source%20Port): A 16-bit field that identifies the port initiating the connection.
- [Destination Port](#Destination%20Port): A 16-bit field that identifies the port receiving the connection.
- [Sequence Number](#Sequence%20Number): A 32-bit field that specifies the first sequence number if the [[#SYN]] flag = 1 or the accumulated sequence number if the [[#SYN]] flag = 0.
- [Acknowledgement Number](#Acknowledgement%20Number): A 32-bit field that specifies the next sequence number the sender of an [[#ACK]] expects (if [[#ACK]] flag = 1).
- [Data Offset](#Data%20Offset): A 4-bit field that specifies the size of the TCP [header](../../structure%20of%20a%20protocol/header.md), with a unit measure of 32-bit words (the minimum value is 5 and the maximum value is 15).
- [Reserved](#Reserved): A 3-bit field reserved for future use, where each bit is set to a value of 0.
- [Flags](#Flags): A series of nine 1-bit fields, each representing a different TCP flag (e.g. The [[#SYN]], [[#ACK]] and [[#URG]] flags).
- [Window Size](#Window%20Size): A 16-bit field indicating the number of bytes the sender of the segment is willing to receive.
- [Checksum](#Checksum): A 16-bit field used for error checking both the [header](../../structure%20of%20a%20protocol/header.md) and the [payload](../../structure%20of%20a%20protocol/payload.md) of the segment.
- [Urgent Pointer](#Urgent%20Pointer): A 16-bit field indicating the last urgent data [byte](../../../reference%20models/OSI%20Model/PDU/other%20data%20units/byte.md) (if [[#URG]] flag = 1).
- [Options](#Options): A field whose size is in the range of 0-320 bits and can be used to indicate a variety of additional TCP options.

### Source Port

The source port is the port the sender selects as the port to send the return traffic to. This is the port the sender will be listening in for the reply. When a client is connecting to a server, a high port number is used. These [port](../../../port.md) are called [ephemeral/dynamic ports](../../../port.md#Ephemeral%20Dynamic%20Ports). The server will usually use the [well-known port](../../../port.md#Well-Known%20Ports) or the [registered port](../../../port.md#Registered%20Ports) number of the service it is running. For example, if it is a web server, port 80 or port 443.

### Destination Port

The destination port is the port you are trying to reach in the remote machine. For example, if you are trying to connect to a web server, the destination port will be port 80 or port 443. If the web server is trying to connect to you, the destination port will likely be a [ephemeral dynamic port](../../../port.md#Ephemeral%20Dynamic%20Ports).

### Sequence Number

The sequence number of the segment being transmitted. If the [[#SYN]] flag is 1, the sequence number is 1 and if the [[#SYN]] flag is 0, the sequence number is the accumulated sequence number, whatever the communication is up to by then.

### Acknowledgement Number

Only populated if [[#ACK]] flag is set to, this is the next sequence number that the sender of the [[#ACK]] expects. 

### Data Offset

This is a measure of the size of the TCP [header](../../structure%20of%20a%20protocol/header.md). The unit of measure if the number of 32 bit words. The minimum possible value is 5 and maximum possible value is 15.

### Reserved

This is a field reserved for future use. As such, its value should always be 000.

### Flags

There are nine 1-bit flags that can be set in this field. They are,
1. [[#NS]]
2. [[#CWR]]
3. [[#ECE]]
4. [[#URG]]
5. [[#ACK]]
6. [[#PSH]]
7. [[#RST]]
8. [[#SYN]]
9. [[#FIN]]

#### NS

#### CWR

#### ECE

#### URG

#### ACK

#### PSH

#### RST

#### SYN

#### FIN

### Window Size

The amount of data that can be sent without expecting an [[#ACK]] is the window size. 

### Checksum

The checksum is used for error checking of both the [header](../../structure%20of%20a%20protocol/header.md) and the [payload](../../structure%20of%20a%20protocol/payload.md).

### Urgent Pointer

Populated if the [[#URG]] flag is set to 1, indicating the last urgent data [byte](../../../reference%20models/OSI%20Model/PDU/other%20data%20units/byte.md) contained in the segment.

### Options

Used to specify different TCP options.