# Internet Protocol (IP)

> Vidath Dissanayake | Sri Lanka

IP runs on the [Internet Layer](../../../../reference%20models/layers/Internet%20Layer.md) of the [TCP/IP Model](../../../../reference%20models/TCP%20IP%20Model/TCP%20IP%20Model.md) and the [Network Layer](../../../../reference%20models/layers/Network%20Layer.md) of the [OSI Model](../../../../reference%20models/OSI%20Model/OSI%20Model.md). It is in charge of delivering IP packets to hosts involved in communication, and it uses [IP address](IP%20address.md)es to identify hosts.

IP uses [encapsulation](../../../../reference%20models/encapsulation.md) to carry upper layer protocols such as [TCP](../../layer%204/TCP.md) and [UDP](../../layer%204/UDP.md).

## IP Header

![IP header](assets/images/IP%20header.png)

The IP [header](../../../structure%20of%20a%20protocol/header.md) is at least 20 [bytes](../../../../reference%20models/OSI%20Model/PDU/other%20data%20units/byte.md) (120 [bits](../../../../reference%20models/OSI%20Model/PDU/bit.md)) and at most 24 [bytes](../../../../reference%20models/OSI%20Model/PDU/other%20data%20units/byte.md) (124 [bits](../../../../reference%20models/OSI%20Model/PDU/bit.md)).

- [Version](#Version) – A 4-[bit](../../../../reference%20models/OSI%20Model/PDU/bit.md) field that identifies the version of IP in use.
- [Source Address](#Source%20Address) – A 32-[bit](../../../../reference%20models/OSI%20Model/PDU/bit.md) field that identifies the [IP address](IP%20address.md) of the device sending the [packet](../../../../reference%20models/OSI%20Model/PDU/packet.md).
- [Destination Address](#Destination%20Address) – A 32-[bit](../../../../reference%20models/OSI%20Model/PDU/bit.md) field that identifies the [IP address](IP%20address.md) of the device recieveing the [packet](../../../../reference%20models/OSI%20Model/PDU/packet.md).

### Version

The first 4 [bits](../../../../reference%20models/OSI%20Model/PDU/bit.md) identify the IP version. It can be used to represent either IPv4 or IPv6.

### Source Address

The 32 [bits](../../../../reference%20models/OSI%20Model/PDU/bit.md) starting at position 96 represents the [IP address](IP%20address.md) of the device that is sending the [packet.](../../../../reference%20models/OSI%20Model/PDU/packet.md)

### Destination Address

The 32 [bits](../../../../reference%20models/OSI%20Model/PDU/bit.md) starting at position 128, which is right after the [Source Address](#Source%20Address), represents the [IP address](IP%20address.md) of the device recieving the [packet](../../../../reference%20models/OSI%20Model/PDU/packet.md).