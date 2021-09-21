# Burp Suite Proxy

The proxy module is the most important one of [[Burp Suite]] [[modules]].

It allows us to capture requests and responses between ourselves and our target. These can then be manipulated or sent to other tools for further processing before being allowed to continue to their destination.


## Intercept

Intercept is on by default in Burp. When a request is captured, it looks like this:

![[request.png]]

At this point, the browser making the request will hang and we can forward (potentially after editing it) or drop the request. We get full control over our traffic.

We can also do various other things here, such as sending the request to one of the other Burp modules, copying it as a cURL command, saving it to a file, etc...

We can disable intercept by clicking the "intercept is on" button.


## HTTP History


## WebSe