# TCP/IP Model

> Vidath Dissanayake | Sri Lanka

When the [OSI Model](OSI%20Model/OSI%20Model.md) was originally developed, it was not clear that we will be primarily running protocols of the TCP/IP suite. There were other contenders besides having [IP addresses](../../communication%20protocol/TCP%20IP%20layer%202/OSI%20layer%203/IP/IP%20address.md) in our devices. However, now it is clear that we are in a [IP](../../communication%20protocol/TCP%20IP%20layer%202/OSI%20layer%203/IP/IP.md) based world, so TCP/IP model might be more suitable.

TCP/IP is a real world application of the network stack and is the protocol stack used in the internet.

The TCP/IP Model is also called the Department of Defence (DOD) Model.

Commonly, this model combines the first 2 layers of the [OSI Model](OSI%20Model/OSI%20Model.md) into one layer and the last 3 layers of the [OSI Model](OSI%20Model/OSI%20Model.md) into another layer.

There are variations of this model with different layer names and different number of layers.

## Four Layer TCP/IP Model

| Layer | Name                                                                                                  | PDU                                                                                           |
| ----- | ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 1     | [Network Access Network Interface Link Layer](#Network%20Access%20Network%20Interface%20Link%20Layer) | Bits                                                                                          |
| 2     | [Internet Layer](#Internet%20Layer)                                                                   | Packets([TCP](../../communication%20protocol/TCP%20IP%20layer%203/OSI%20layer%204/TCP.md))/Datagrams([UDP](../../communication%20protocol/TCP%20IP%20layer%203/OSI%20layer%204/UDP.md)) |
| 3     | [Transport Layer](#Transport%20Layer)                                                                 | Segments                                                                                      |
| 4     | [Application Layer](#Application%20Layer)                                                             | Data                                                                                          |

### Network Access/Network Interface/Link Layer

### Internet Layer

### Transport Layer

### Application Layer

## Five Layer TCP/IP Model

| Layer | Name                                                                            | PDU                                                                                           |
| ----- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| 1     | [Physical Layer](#Physical%20Layer)                                             | Bits                                                                                          |
| 2     | [Data Link/Network Interface Layer](#Data%20Link%20Network%20Interface%20Layer) | Frames                                                                                        |
| 3     | [Internet Layer](#Internet%20Layer)                                             | Packets([TCP](../../communication%20protocol/TCP%20IP%20layer%203/OSI%20layer%204/TCP.md))/Datagrams([UDP](../../communication%20protocol/TCP%20IP%20layer%203/OSI%20layer%204/UDP.md)) |
| 4     | [Transport Layer](#Transport%20Layer)                                           | Segments                                                                                      |
| 5     | [Application Layer](#Application%20Layer)                                       | Data                                                                                          |

### Physical Layer

### Data Link/Network Interface Layer
