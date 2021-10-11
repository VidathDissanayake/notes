# Symmetric Ciphers

Symmetric ciphers are the building blocks of secure communication.

In symmetric ciphers, the two parties share a secret key (_k_) that only they know.

The cipher will contain an encryption algorithm (_E_) and a decryption algorithm(D).

_E_ takes the message (_m_) and _k_ as input and produces a ciphertext (_c_).

_D_ takes _c_ and _k_ as input and produces the message.

There are 2 types of keys used in symmetric ciphers.
1. Single use key (one time key)
    - key is only used to encrypt one message.
        - 
2. Multi use key (many time key)