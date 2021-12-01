
# SSL (Secure Socket Layer)

Before we talk about TLS, it is important to talk about its predecessor, SSL.

Netscape developed the original SSL protocols, and Taher Elgamal, chief scientist at Netscape Communications from 1995 to 1998, has been described as the "Father of SSL".

SSL had 3 versions.

|Protocol| Published |Deprecated|
|:------:|:---------:|:--------:|
|SSL 1.0 |Unpublished|          |
|SSL 2.0 |   1995    |   2011   |
|SSL 3.0 |   1996    |   2015   |

SSL is no longer in use, as it has severe security flaws.


# TLS (Transport Layer Security)

TLS (Transport Layer Security) is the successor to SSL. However, SSL is widely known, so SSL is used to refer to TLS too.

These are slightly different protocols. TLS is essentially an improved version of SSL.

TLS has 4 versions that have been released as of the time of writing.

|Protocol|Published|Deprecated|
|:------:|:-------:|:--------:|
|TLS 1.0 |  1999   |   2020   |
|TLS 1.1 |  2006   |   2020   |
|TLS 1.2 |  2008   |          |
|TLS 1.3 |  2018   |          |

TLS has 2 parts.
1. Handshake Protocol - Establish shared secret key using public key [cryptography](../../cryptography.md).
2. Record Layer - Transmit data using shared secret key. Ensures [confidentiality](../../../principles%20and%20standards%20of%20infosec/CIA%20triad/CIA%20triad.md#Confidentiality) and [integrity](../../../principles%20and%20standards%20of%20infosec/CIA%20triad/CIA%20triad.md#Integrity).

## Handshake Protocol

## Record Layer