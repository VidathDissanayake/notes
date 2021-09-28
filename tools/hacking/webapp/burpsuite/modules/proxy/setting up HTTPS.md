# Setting up HTTPS in Burp Suite Proxy Module

To use HTTPS functionality in [[Burp Suite]] [[Proxy]] module, there is some setting up that needs to be done.

Portswigger **C**ertificate **A**uthority (CA) (The one used by Burp) isn't authorized to secure the connection on browsers, as it isn't in the trusted list.

We have to manually add the CA certificate to our list of trusted certificate authorities.

We need to,
1. Get the certificate.
2. Import the cer