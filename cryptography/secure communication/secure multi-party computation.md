# Secure Multi-Party Computation

> Vidath Dissanayake | Sri Lanka  
> Tags: #crypto #crypto/secure_com  
> Links: [secure communication](secure%20communication.md)  
> Sources:  

The goal of secure multi-party computation is to take the secret input of multiple parties and take use a function on those inputs to determine a value while keeping all else secret.

E.g. 
1. In an election, the number of votes and the winner should be taken while keeping the identity and all other details about voters anonymous. (Votes are inputs and the function is majority)
2. In a private auction, the highest bidder and the second-highest bid should be taken while keeping the highest bid and other's identities hidden. (Bids are input and function is second-largest number)

There are a few ways to achieve this.
1. [Using a Trusted Authority](#Using%20a%20Trusted%20Authority)
2. [Without a Trusted Authority](#Without%20a%20Trusted%20Authority)

---

## Using a Trusted Authority

> Links: [trusted authority](trusted%20authority.md)  
> Sources:  

The [trusted authority](trusted%20authority.md) will collect all inputs and will publish the value of the function after it figures it out.

So the value of the function will become public, but only the [trusted authority](trusted%20authority.md) will know all the other information.

The downside is that you have to trust the authority. If for some reason it is untrustworthy, then all data is in danger.

---

## Without a Trusted Authority

> Links:  
> Sources:  

To achieve this without a [trusted authority](trusted%20authority.md),

---