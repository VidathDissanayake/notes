# Setting up HTTPS in Burp Suite Proxy Module

> Vidath Dissanayake | Sri Lanka

To use HTTPS functionality in [Burp Suite](../../Burp%20Suite.md) [Proxy](Proxy.md) module, there is some setting up that needs to be done.

Portswigger **C**ertificate **A**uthority (CA) (The one used by Burp) isn't authorized to secure the connection on browsers, as it isn't in the trusted list.

We have to manually add the CA certificate to our list of trusted certificate authorities.

We need to,
1. Download the certificate.
2. Import the certificate to the browser.

First, with the [Proxy](Proxy.md) activated, head to [http://burp/cert](http://burp/cert); this will download a file called `cacert.der`.

Then find the place where you can upload the certificate in your browser (search in settings/preferences) and upload it as a Trusted Certificate Authority certificate.