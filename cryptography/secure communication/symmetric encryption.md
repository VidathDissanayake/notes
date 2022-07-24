# Symmetric Ciphers

> Vidath Dissanayake | Sri Lanka  
> Tags: #crypto #crypto/secure_com  
> Links: [secure communication](secure%20communication.md)  
> Sources:  

Symmetric ciphers are the building blocks of [secure communication](secure%20communication.md).

In symmetric ciphers, the two parties share a secret key (_k_) that only they know.

The cipher will contain an encryption algorithm (_E_) and a decryption algorithm(D).

_E_ takes the message (_m_) and _k_ as input and produces a ciphertext (_c_).

_D_ takes _c_ and _k_ as input and produces the message.

There are 2 types of keys used in symmetric ciphers.
1. Single use key (one time key)
    - Key is only used to encrypt one message.
        - e.g. Encrypted email (new key generated for every email)
2. Multi use key (many time key)
    - Key used to encrypt multiple messages.
        - e.g. Encrypted files (same key used to encrypt many files)
    - Need more resources. 

---