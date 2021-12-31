# Secure Communication

> Vidath Dissanayake | Sri Lanka

When data is being communicated, [cryptography](../cryptography.md) is used to make sure that an attacker can't eavesdrop or tamper with the data being exchanged.

For example, when [web traffic](web%20traffic.md) is being transmitted, [TLS](protocols/TLS.md) is used to encrypt the insecure HTTP protocol and convert it into the secure HTTPS protocol.

The building block of secure communication is [symmetric encryption](symmetric%20encryption.md).

The core of [cryptography](../cryptography.md) for secure communication consists of two parts.
1. Secret key establishment
2. Secure communication


## Secure Key Establishment

After the protocol to establish the shared key, both parties will know the shared key, and know that they are in fact talking to one another but an attacker listening in on the conversation will not know what the key is.


## Secure Communication Using Shared Key.

After the shared key is established, the two parties will communicate using encryption algorithms that encrypts the data being communicated using the shared key so that an attacker can't,
- understand the messages being sent.
- tamper with the data being sent.

In other words, these encryption schemes provide both confidentiality and integrity.