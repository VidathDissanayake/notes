# IP Address

> Vidath Dissanayake | Sri Lanka

Similar to mail, [IP](IP.md) uses an addressing scheme to deliver packets to the right destination.

An [Internet Protocol (IP)](IP.md) address can be used as a way of identifying a host on a [network](../../../../network.md) for a period of time.

Then that IP address can then be associated with another device without the IP address changing.

IP addresses exist in the [Network Layer](../../../../reference%20models/layers/Network%20Layer.md) of the [OSI Model](../../../../reference%20models/OSI%20Model/OSI%20Model.md).

There are 2 versions of IP Addresses.
- IPv4 addresses
- IPv6 addresses

---

## IPv4 Addresses

***Note: Generally, an "IP address" is an IPv4 address unless specified as IPv6.***

An IP address is a 32 bit number that is divided into four octets of 8 bits each.

![ipv4 octets](assets/images/ipv4%20octets.png)

IPv4, uses a numbering system of 2^32 IP addresses (4.29 billion).

This number is calculated through a technique known as IP addressing & subnetting.

IP addresses can change from device to device but cannot be active simultaneously more than once within the same [network](../../../../network.md).

There are 2 types of IP address ranges.
- Public IP addresses
- Private IP addresses

Depending on the location of the device, the IP address can be private or public.

A public address is used to identify the device on [the Internet](../../../../the%20Internet/the%20Internet.md), whereas a private addss is used to identify a device amongst other devices in a [private network](../../../../types%20of%20networks/private%20network.md).

|Device Name     |IP Address   |IP Address Type|
|:--------------:|:-----------:|:-------------:|
|DESKTOP-KJE57FD |192.168.1.77 |Private        |
|DESKTOP-KJE57FD |86.157.52.21 |Public         |
|CMNatic-PC      |192.168.1.74 |Private        |
|CMNatic-PC      |86.157.52.21 |Public         |

These two devices will be able to use their private IP addresses to communicate with each other.

However, any data sent to [the Internet](../../../../the%20Internet/the%20Internet.md) from either of these devices will be identified by the same public IP address. Public IP addresses are given by the Internet Service Provider (ISP) at a monthly fee.

---

## IPv6 Addresses

As more and more devices become connected, it is becoming increasingly harder to get a public address that isn't already in use.

Cisco estimated that there will be approximately 50 billion devices connected to [the Internet](../../../../the%20Internet/the%20Internet.md) by the end of 2021.

IPv6 is a new iteration of the Internet Protocol addressing scheme to help tackle this issue.

IPv6 has a few benefits.
- Supports up to 2^128 of IP addresses (340 trillion-plus)
- More efficient due to new methodologies

![ipv6](assets/images/ipv6.png)