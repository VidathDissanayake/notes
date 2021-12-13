# OSI Model

The OSI Model or the Open Systems Interconnect Model is one of the most famous network reference models.

It is made up of 7 layers. These layers have different names, and the information passing through different layers are referred to using different names called PDUs (Protocol Data Units). The first 4 layers have different PDUs and the last 3 have the same PDU - Data. To remember, the PDUs of 1st 4 layers, we can use the following mnemonic device.

**B**acon **F**rying **P**roduces **S**alvation.

- Bacon - Bits
- Frying - Frames
- Produces - Packets
- Salvation - Segments

| Layer | Name                                        | PDU                         |
| ----- | ------------------------------------------- | --------------------------- |
| 1     | [Physical Layer](#Physical%20Layer.md)      | Bits                        |
| 2     | [Data Link Layer](#Data%20Link%20Layer)     | Frames                      |
| 3     | [Network Layer](#Network%20Layer)           | Packets(TCP)/Datagrams(UDP) |
| 4     | [Transport Layer](#Transport%20Layer)       | Segments                    |
| 5     | [Session Layer](#Session%20Layer)           | Data                        |
| 6     | [Presentation Layer](#Presentation%20Layer) | Data                        |
| 7     | [Application Layer](#Application%20Layer)   | Data                        |

It is important to understand that every protocol doesn't fit neatly into a single layer. This is not the reality. There are protocols that work over multiple layers. **This is a reference model, not a reverence model!**

To memorize these layers, the following mnemonic devices can be used.

From Layer 1 to 7,

- **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way
  1. Please - Physical
  2. Do - Data Link
  3. Not - Network
  4. Throw - Transport
  5. Sausage - Session
  6. Pizza - Presentation
  7. Away - Application

From layer 7 to 1,

- **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing
  1. All - Application
  2. People - Presentation
  3. Seem - Session
  4. To - Transport
  5. Need - Network
  6. Data - Data Link
  7. Processing - Physical

## Physical Layer

This layer is concerned with getting bits on the wire. This is the physical hardware components such as copper wires and fibre optic cables.

## Data Link Layer

This layer makes decisions on an Ethernet network based on [MAC addresses](../MAC%20address.md). Devices such as Ethernet switches belong to this layer.

## Network Layer

Routers usually live in this layer. They make informed decisions based on [IP addresses](../IP%20address.md). A protocol used in this layer is the [Internet Protocol (IP).](../protocols/network%20layer/IP.md)

## Transport Layer

This layer is concerned with network connections. There are 2 basic types of connections.

- Connection Oriented (Reliable) Connections
- Connection Less (Unreliable) Connections

Transmission Control Protocol (TCP) is a reliable connection protocol and User Datagram Protocol (UDP) is an unreliable connection protocol used in this layer.

## Session Layer

This layer is concerned with setting up, maintaining and tearing down a session. An example of a protocol in this layer would be Session Initiation Protocol (SIP).

## Presentation Layer

This layer is about how data is presented or formatted. Examples would be JPEG/PNG for images and ASCII 8 for text.

## Application Layer

This layer is where application protocols that provide network functionality are. Examples are, HTTP used for insecure web browsing using TCP port 80 and HTTPS used for secure web browsing using TCP port 443.
