# OSI Model

> Vidath Dissanayake | Sri Lanka

The OSI Model or the Open Systems Interconnect Model is one of the most famous [network](../../network.md) [reference model](reference%20model.md).

It is made up of 7 layers. These layers have different names, and the information passing through different layers are referred to using different names called PDUs (Protocol Data Units). The first 4 layers have different PDUs and the last 3 have the same PDU – Data. To remember, the PDUs of 1st 4 layers, we can use the following mnemonic device.

**B**acon **F**rying **P**roduces **S**alvation.

- Bacon – Bits
- Frying – Frames
- Produces – Packets
- Salvation – Segments

| Layer | Name                                                 | PDU                                                                                                                               |
| ----- | ---------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1     | [Physical Layer](../layers/Physical%20Layer.md)         | [Bit](PDU/bit.md)                                                                                                                              |
| 2     | [Data Link Layer](../layers/Data%20Link%20Layer.md)     | Frame                                                                                                                            |
| 3     | [Network Layer](../layers/Network%20Layer.md)           | [Packet](PDU/packet.md)([TCP](../../communication%20protocol/TCP%20IP%20layer%203/OSI%20layer%204/TCP.md))/Datagram([UDP](../../communication%20protocol/TCP%20IP%20layer%203/OSI%20layer%204/UDP.md)) |
| 4     | [Transport Layer](../layers/Transport%20Layer.md)       | Segment                                                                                                                          |
| 5     | [Session Layer](../layers/Session%20Layer.md)           | Data                                                                                                                              |
| 6     | [Presentation Layer](../layers/Presentation%20Layer.md) | Data                                                                                                                              |
| 7     | [Application Layer](../layers/Application%20Layer.md)   | Data                                                                                                                              |

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