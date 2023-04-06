# Options for Configuring Burp Suite

> Vidath Dissanayake | Sri Lanka
> Tags: #tools/hacking/web_app 
> Links: [Burp Suite](Burp%20Suite.md)

There are two main types of options in [Burp Suite](Burp%20Suite.md).
- Global settings (User options tab).
- Project-specific settings (Project options tab)

## User Options

User options apply every time Burp is opened.

The settings here apply globally. They control the application. However, most of them can be overridden by [Project Options](#Project%20Options).

There are four main subsections of the User options tab:
- **Connections** allow us to control how Burp makes connections to targets. (E.g: Through a proxy.)
- **TLS** allows us to enable and disable various [TLS](../../../../cryptography/secure%20communication/secure%20communication%20protocols/TLS.md) options. We can also upload client certificates there if needed.
- **Display** allows us to change how [Burp Suite](Burp%20Suite.md) looks. (E.g. Font, scale, dark mode.) Also allows configuring things like the rendering engine in [Repeater](modules/Repeater/Repeater.md).
- **Misc** contains settings including the key bindings table (HotKeys), temp file location, proxy behaviour and other general settings. You can configure auto backup and REST API in [Burp Suite Professional Edition](editions.md#Burp%20Suite%20Professional%20Edition).

## Project Options

Project options will only apply to the current project.

The options here can be used to override settings in [User Options](#User%20Options).

There are five main subsections of the Project options tab:
- **Connections** have many of the same options as the User options equivalent. It also has "Hostname Resolution" used to override default DNS resolution and map domains to IPs.
- **HTTP** defines how Burp handles various aspects of the HTTP protocol: for example, whether it follows redirects or how to handle unusual response codes.
- **TLS** have many of the same options as the User options equivalent. It also shows the server certificates of sites we have visited.
- **Sessions** provides the options for handling sessions. It allows us to define how Burp obtains, saves, and uses session cookies that it receives from target sites. It also allows us to define macros which we can use to automate things such as logging into web applications (giving us an instant authenticated session, assuming we have valid credentials).
- **Misc** allows to control logging and embedded browser behaviour. It also allows configuring Colab server and scheduled tasks in [Burp Suite Professional Edition](editions.md#Burp%20Suite%20Professional%20Edition).