# ICMP Ping

Ping is one of the most fundamental network tools.

Ping uses **ICMP (Internet Control Message Protocol) echo** packets to determine the performance of a connection between devices.
- ICMP echo **request** from local machine.
- ICMP echo **reply** from target machine.

The **time taken** for ICMP packets travelling between devices is measured by ping.

Pings can be performed against **network devices** or **resources like websites**.

Ping is usually **pre-installed** in almost all OSs.

**Syntax:**
```bash
# Ping an IP address
ping IP_ADDRESS

# Ping an URL
ping URL
```

**Example:**
![ping](ping.png)