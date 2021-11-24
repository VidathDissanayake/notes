# Burp Suite Browser

[Burp Suite](Burp%20Suite.md) comes with a Chromium browser that is pre-configured to use the Burp [Proxy](Proxy.md).

We can start the Burp Browser with the "Open Browser" button in the proxy tab:
![open browser](assets/images/open%20browser.png)

If we are running on Linux as the root user, Burp Suite is unable to create a sandbox environment to start the Burp Browser in, causing it to throw an error and die:
![browser sandbox error](assets/images/browser%20sandbox%20error.png)

There are two simple solutions to this:

-   **The smart option:** We could create a new user and run Burp Suite under a low privilege account.
-   **The easy option:** We could go to `Project options -> Misc -> Embedded Browser` and check the `Allow the embedded browser to run without a sandbox` option. Checking this option will allow the browser to start, but be aware that it is disabled by default for security reasons: if we get compromised using the browser, then an attacker will have access to our entire machine.