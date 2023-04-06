# ICMP Ping

> Vidath Dissanayake | Sri Lanka
> Tags: #tools/networking 
> Links: [networking tools](networking%20tools.md)

Ping is one of the most fundamental network tools.

Ping uses [ICMP](../../network/communication%20protocol/TCP%20IP%20layer%202/OSI%20layer%203/ICMP.md) (Internet Control Message Protocol) echo packets to determine the performance of a connection between devices. It happens as follows.

1. [ICMP](../../network/communication%20protocol/TCP%20IP%20layer%202/OSI%20layer%203/ICMP.md) echo request from local machine.
2. [ICMP](../../network/communication%20protocol/TCP%20IP%20layer%202/OSI%20layer%203/ICMP.md) echo reply from target machine.

The time taken for [ICMP](../../network/communication%20protocol/TCP%20IP%20layer%202/OSI%20layer%203/ICMP.md) packets travelling between devices is measured by ping.

Pings can be performed against [network device](../../network/devices/network%20device.md) or resources like websites.

Ping is usually pre-installed in almost all OSes.

**Syntax:**

```bash
# Ping an IP address
ping IP_ADDRESS

# Ping an URL
ping URL
```

**Example:**
![ping](assets/images/ping.png)
