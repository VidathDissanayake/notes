# Encapsulation

> Vidath Dissanayake | Sri Lanka

Encapsulation is the way in which lower layer [communication protocols](../communication%20protocol/communication%20protocol.md) carry the higher layer protocols, each with their own [header](../communication%20protocol/structure%20of%20a%20protocol/header.md) and [payload](../communication%20protocol/structure%20of%20a%20protocol/payload.md), within them. This means that the entire upper protocol which consists of a [header](../communication%20protocol/structure%20of%20a%20protocol/header.md) and a [payload](../communication%20protocol/structure%20of%20a%20protocol/payload.md) becomes the [payload](../communication%20protocol/structure%20of%20a%20protocol/payload.md) of the lower layer protocol.

The receiving host will reverse this. Each layer will remove the header of that layer and pass the payload to the layer above.


## TCP/IP Encapsulation

![TCP IP encapsulation](assets/images/TCP%20IP%20encapsulation.png)

Here, the [Application Layer](layers/Application%20Layer.md) gives its [packet](OSI%20Model/PDU/packet.md) to the [Transport Layer](layers/Transport%20Layer.md), which will use it as the payload and add its own header. This is done in all the layers to every packet.

![TCP IP encapsulation true view](assets/images/TCP%20IP%20encapsulation%20true%20view.png)