# Options for Configuring Burp Suite

There are two main types of options in [[Burp Suite]].
- Global settings (User options tab).
- Project-specific settings (Project options tab)

## User Options

User options apply every time Burp is opened.

The settings here apply globally. They control the application. However, most of them can be overridden by [[#Project Options]].

There are four main sub-sections of the User options tab:
- **Connections** allow us to control how Burp makes connections to targets. (Eg: Through a proxy.)
- **TLS** allows us to enable and disable various TLS options.We can also upload client certificates there if needed.
- **Display** allows us to change how Burp Suite looks. (E.g. Font, scale, dark mode.) Also allows to configure things like the rendering engine in [[Repeater]].
- **Misc** contains settings including the keybindings table (HotKeys).

## Project Options

Project options will only apply to the current project.

The options here can be used to override settings in [[#User Options]].

There are five main sub-sections of the Project options tab:
- **Connections** have many of the same options as the User options equivalent. It also has "Hostname Resolution" used to override default DNS resolution and map domains to IPs.
- **HTTP** defines how Burp handles various aspects of the HTTP protocol: for example, whether it follows redirects or how to handle unusual response codes.
- **TLS**  have many of the same options as the User options equivalent. It also shows the server certificates of sites we have visited.
- **Sessions** tab provides us with options for handling sessions. It allows us to define how Burp obtains, saves, and uses session cookies that it receives from target sites. It also allows us to define macros which we can use to automate things such as logging into web applications (giving us an instant authenticated session, assuming we have valid credentials).