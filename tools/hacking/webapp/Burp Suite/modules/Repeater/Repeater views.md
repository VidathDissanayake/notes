# Response and Request Views

> Vidath Dissanayake | Sri Lanka

[Repeater](Repeater.md) offers us various ways to present the responses to our requests -- these range from [hex](../../../../../../general/encoding%20and%20decoding/hex/hex.md) output all the way up to a fully rendered version of the page.

We can see the available options by looking above the response box:

![The four view buttons above the response text](assets/images/response%20views.png)  

We have four display options here:

1.  **Pretty:** This is the default option. It takes the raw response and attempts to beautify it slightly, making it easier to read.
2.  **Raw:** The pure, un-beautified response from the server.
3.  **Hex:** This view takes the raw response and gives us a [byte](../../../../../../network/reference%20models/OSI%20Model/PDU/other%20data%20units/byte.md) view of it -- especially useful if the response is a binary file.
4.  **Render (Only for response):** The render view renders the page as it would appear in your browser.

---

Just to the right of the view buttons is the "Show non-printable characters" button (`\n`). 

This button allows us to display characters that usually wouldn't show up in the Pretty or Raw views. 

For example, every line in the response will end with the characters `\r\n` -- these signify a carriage return followed by a newline and are part of how HTTP headers are interpreted.