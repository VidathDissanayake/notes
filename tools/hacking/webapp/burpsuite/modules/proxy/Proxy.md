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

Burp Suite will still (by default) be logging requests made through the proxy when the intercept is off. This can be very useful for going back and analysing prior requests, even if we didn't specifically capture them when they were made.

These logs can be viewed by going to the "HTTP history" sub-tab. These requests can also be sent to other modules...


## WebSockets History

Like [[#HTTP History]] Burp will also capture and log WebSocket communication which can be exceedingly helpful when analysing a web app.

These logs can be viewed by going to the "WebSockets history" sub-tab. These can also be sent to other modules.


## Options

Proxy specific options can be found in the "Options" sub-tab.

We can set which requests will be intercepted and any automatic replacing we need to do here.

There are also request modification rules and other general settings.