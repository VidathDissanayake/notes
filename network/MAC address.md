# MAC Addresses

> Vidath Dissanayake | Sri Lanka

All network interface cards ([NIC](devices/layer%202/NIC.md)s) have a unique 12 character 48 bit hexadecimal number address hardcoded in it.

These 12 characters are separated into 6 groups of 2 with colons (:) as separators.

This address is known as the Media Access Control (MAC) address.

A MAC address is composed of 2 main sections.
1. Organizationally Unique Identifier (OUI)
    - The 1st 24 bits (6 characters or 3 parts) represent the company that made the network interface.
    - This is known as the Organizationally Unique Identifier (OUI)
2. Device ID
    - The remaining part is the Device ID. This is unique to your [NIC](devices/layer%202/NIC.md).

![mac address](assets/images/mac%20address.png)