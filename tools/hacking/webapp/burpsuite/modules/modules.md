# Modules in the Burp Suite Framework

Main tools in the [Burp Suite](Burp%20Suite.md) framework 

- **Dashboard:** [Dashboard](Dashboard.md) gives a overview of what Burp is duing.
- **Target:** [Target](Target.md) allows to set the scope and creates a site map.
- **Proxy:** [Proxy](Proxy.md) allows us to intercept and modify requests/responses when interacting with web applications.
- **Intruder:** [Intruder](Intruder) allows us to spray an endpoint with requests. Used for [bruteforcing](bruteforcing) and [fuzzing](fuzzing).
- **Repeater:** [Repeater](Repeater.md) allows us to capture, modify, then resend the same request numerous times.
- **Sequencer:** [Sequencer](Sequencer) is used for assessing the randomness of tokens such as session cookie values or other supposedly random generated data.
- **Decoder:** [Decoder](Decoder) provides the ability to transforming data. Either in terms of [decoding](decoding) captured information, or [encoding](encoding) a payload prior to sending it to the target.
- **Comparer:** [Comparer](Comparer) allows us to compare two pieces of data at either word or byte level.
- **Logger:** [Logger](Logger) logs all traffic.
- **Extender:** [Extender](Extender.md) allows quickly and easily load [extensions](extensions.md) into the framework, as well as providing a marketplace to download third-party modules (referred to as the "BApp Store").