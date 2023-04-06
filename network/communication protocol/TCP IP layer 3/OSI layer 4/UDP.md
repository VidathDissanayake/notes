# User Datagram Protocol (UDP)

> Vidath Dissanayake | Sri Lanka

UDP is not considered as a reliable protocol as it is a connectionless protocol. We do not get conformation whether the [packet](../../../reference%20models/OSI%20Model/PDU/packet.md) was received. However, the speed of the [data](../../../reference%20models/OSI%20Model/PDU/data.md) transfer is higher than a connection oriented protocol such as [TCP](TCP.md), as there is no waiting for conformation. The [header](../../structure%20of%20a%20protocol/header.md) of UDP is also much smaller, and there is much less overhead when using UDP than [TCP](TCP.md).

Therefore, UDP is used in situations where reliability is not as important as speed as well as in instances where retransmission is not preferable For example,
- VoIP calls


## UDP Header

Below is a visual representation of the UDP [header](../../structure%20of%20a%20protocol/header.md).

![udp header](assets/images/udp%20header.png)

- [Source Port](#Source%20Port): A 16-[bit](../../../reference%20models/OSI%20Model/PDU/bit.md) field that identifies the [port](../../../port.md) initiating the connection.
- [Destination Port](#Destination%20Port): A 16-[bit](../../../reference%20models/OSI%20Model/PDU/bit.md) field that identifies the [port](../../../port.md) receiving the connection.
- [Length](#Length):
- [Checksum](#Checksum): A 16-[bit](../../../reference%20models/OSI%20Model/PDU/bit.md) field used for error checking both the [header](../../structure%20of%20a%20protocol/header.md) and the [payload](../../structure%20of%20a%20protocol/payload.md) of the [segment](../../../reference%20models/OSI%20Model/PDU/segment.md).

### Source Port

### Destination Port

### Length

### Checksum