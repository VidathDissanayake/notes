# VPS

> Vidath Dissanayake | Sri Lanka  
> Tags: #infrastructure
> Links: [Infrastructure](Infrastructure.md)
> Sources

---

A VPS or a virtual private server is a private computer on the cloud that the user can access and do as they please.

Oracle Cloud free tier has an always free VPS server. 

## Oracle Cloud Free VPS

> Links:
> Sources: [Oracle Cloud Free Tier](https://www.oracle.com/cloud/free) 

First, go to the above link and create a free account. A credit or debit card is needed.

### Ampere A1 ARM VPS

> Sources: [Free VPS with 4 OCPU, 24GB RAM and 200GB storage [ENG ]](http://blog.tomaszdunia.pl/oracle-free-tier-eng/)

Oracle allows creating an arm VPS with up to 4 CPU cores and 24 GB of memory for free.

In the home page, scroll down and click on *Create a VM instance*.
![Create a VM instance](assets/images/Create%20a%20VM%20instance.png)

Change the name to something you want. Leave *Placement* and *Security* as defaults.

![VM Config ARM 1](assets/images/VM%20Config%20ARM%201.png)

On *Image and Shape*, Click *Change Image* and Select **Ubuntu 22.04**. I found that 24.04 and 22.04 Minimal doesn't have arm images as of yet for this.

![Select Ubuntu 22.04](assets/images/Select%20Ubuntu%2022.04.png)

Next click *Change Shape*. For the *Shape Series* select **Ampere**. Select **VM.Standard.A1.Flex** as the *Shape name*. Change the *Number of OCPUs* to **4** and ensure that *Amount of memory (GB)* is **24**. 

![Select Shape](assets/images/Select%20Shape.png)

*In primary VNIC information*, leave the defaults to create VM in root network. Or create a new network with any name you want.

![Primary VNIC information](assets/images/Primary%20VNIC%20information.png)

The rest is pretty obvious. Too lazy to complete this. Read and complete and create. You can also do the same but change the shape to *VM.Standard.E2.1.Micro* to create an AMD VM.