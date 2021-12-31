# ICMP Ping

> Vidath Dissanayake | Sri Lanka

Ping is one of the most fundamental network tools.

Ping uses [ICMP](../../network/protocols/layer%203/ICMP.md) (Internet Control Message Protocol) echo packets to determine the performance of a connection between devices. It happens as follows.

1. [ICMP](../../network/protocols/layer%203/ICMP.md) echo request from local machine.
2. [ICMP](../../network/protocols/layer%203/ICMP.md) echo reply from target machine.

The time taken for [ICMP](../../network/protocols/layer%203/ICMP.md) packets travelling between devices is measured by ping.

Pings can be performed against [network devices](../../network/devices/network%20devices.md) or resources like websites.

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
