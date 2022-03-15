# Modules in the Burp Suite Framework

> Vidath Dissanayake | Sri Lanka
> Tags: #tools/hacking/web_app
> Links: [Burp Suite](../Burp%20Suite.md)

Main tools in the [Burp Suite](../Burp%20Suite.md) framework 

- **Dashboard:** [Dashboard](Dashboard/Dashboard.md) gives an overview of what Burp is doing.
- **Target:** [Target](Target/Target.md) allows to set the scope and creates a site map.
- **Proxy:** [Proxy](Proxy/Proxy.md) allows us to intercept and modify requests/responses when interacting with web applications.
- **Intruder:** [Intruder](Intruder/Intruder.md) allows us to spray an endpoint with requests. Used for bruteforcing and fuzzing.
- **Repeater:** [Repeater](Repeater/Repeater.md) allows us to capture, modify, then resend the same request numerous times.
- **Sequencer:** [Sequencer](Sequencer/Sequencer.md) is used for assessing the randomness of tokens such as session cookie values or other supposedly random generated data.
- **Decoder:** [Decoder](Decoder/Decoder.md) provides the ability to transforming data. Either in terms of [decoding](../../../../../general/encoding%20and%20decoding/decoding.md) captured information, or [encoding](../../../../../general/encoding%20and%20decoding/encoding.md) a [payload](../../../../../network/communication%20protocol/structure%20of%20a%20protocol/payload.md) prior to sending it to the [Target](Target/Target.md).
- **Comparer:** [Comparer](Comparer/Comparer.md) allows us to compare two pieces of data at either word or [byte](../../../../../network/reference%20models/OSI%20Model/PDU/other%20data%20units/byte.md) level.
- **Logger:** [Logger](Logger/Logger.md) logs all traffic.
- **Extender:** [Extender](Extender/Extender.md) allows quickly and easily load [Burp extensions](Extender/Burp%20extensions.md) into the framework, as well as providing a marketplace to download third-party modules (referred to as the "BApp Store").