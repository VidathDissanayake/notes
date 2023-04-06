# Substitution Cipher

> Vidath Dissanayake | Sri Lanka  
> Tags: #crypto #crypto/history #crypto/history/ciphers  
> Links: [history of cryptography](../history%20of%20cryptography.md)  
> Sources:  

A substitution cipher is a symmetric cipher where each character is mapped to a different character. This mapping is defined in the key called the substitution table.

---

## Breaking Substitution Cipher

> Links: [ciphertext only attack](../../cryptographic%20attacks/ciphertext%20only%20attack.md)  
> Sources:  

Let's assume that the substitution cipher uses the English language and only the 26 letters of the English alphabet. This will mean that the key space is 26! (26 factorial). 26! is roughly 2^88, which means the substitution cipher key is about 88 bits. This is a pretty large key space.

So, to crack the cipher, we can use letter frequencies.

"e" is the most common letter in the English language. It appears about 12.7% of the time. So, it is highly likely that the most occurring letter in the ciphertext represents plaintext "e". We can do the same for letters "t" and "a" which are the 2nd and 3rd most common letters at 9.1% and 8.1% respectively.

Other letters appear almost the same amount, apart from rate letters such as "q" and "x". So, to decrypt the rest, we can use common letter pairs (digrams) and letter triplets (trigrams) and so on...

So, substitution cipher is vulnerable to the worst possible type of attack, which is a [ciphertext only attack](../../cryptographic%20attacks/ciphertext%20only%20attack.md).

---