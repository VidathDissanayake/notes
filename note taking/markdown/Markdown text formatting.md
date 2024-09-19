# Text Formatting

> Vidath Dissanayake | Sri Lanka  
> Tags: #markdown  
> Links: [markdown](markdown.md)  
> Sources:  

Text formatting syntax in [markdown](markdown.md).

---

## Paragraphs

> Links:  
> Sources:  

To create paragraphs, use a blank line to separate one or more lines of text. Do not add indentation infront of paragraphs unless they are in a list to avoid unexpected formatting problems.

**Syntax:**

```md
This is the first paragraph.

This is the second paragraph.
```

**Output:**

This is the first paragraph.

This is the second paragraph.

---

## Line Breaks

> Links:  
> Sources:  

`Two spaces` at the end of the line before pressing `enter` will cause a line break.

`Backslash` (`\`) at the end of line will also cause line breaks. (**May not be available in every application.**)

**Syntax:**

```md
This is the first line.  
And this is the second line.

This is the first line. \
And this is the second line.
```

**Output:**

This is the first line.  
And this is the second line.

This is the first line. \
And this is the second line.

---

## Bold

> Links:  
> Sources:  

To make text bold, surround the text with `two asterisks` (`**`) or `two underscores` (`__`).

To bold the middle of a word for emphasis, add `two asterisks` (`**`) without spaces around the letters.

**Syntax:**

```md
This is **bold text**.

This is __bold text__.

This**is**bold	
```

**Output:**

This is **bold text**.

This is __bold text__.

This**is**bold.

---

## Italic

> Links:  
> Sources:  

To make text italic, surround the text with `an asterisk` (`*`) or `an underscore` (`_`).

To italicize the middle of a word for emphasis, add `an asterisk` (`*`) without spaces around the letters.

**Syntax:**
```md
This is italicized *text*.

This is italicized _text_.

This*is*italic.
```

**Output:**

This is italicized *text*.

This is italicized _text_.

This*is*italic.

---

## Bold and Italic

> Links:  
> Sources:  

To emphasize text with bold and italics at the same time, add `three asterisks` (`***`) or `three underscores` (`___`) around the word.

`Two astersiks` and `an underscore` (`**_`,`_**`) or `two underscores` and `an astersik` (`__*`,`*__`) can also be used.

To bold and italicize the middle of a word for emphasis, add `three asterisks` (`***`) without spaces around the letters.

**Syntax:**

```md
This text is ***very important***.

This text is ___very important___.

This text is **_very important_**.

This text is __*very important*__.

This text is *__very important__*.

This text is _**very important**_.

This is actually***very***important text.
```

**Output:**

This text is ***very important***.

This text is ___very important___.

This text is **_very important_**.

This text is __*very important*__.

This text is *__very important__*.

This text is _**very important**_.

This is actually***very***important text.

---

## Blockquotes

> Links:  
> Sources:  

To put text in a blockquote, prepend with `>` and a `space`. 

Blockquotes can be nested by adding more `>` s. 

Blockquotes can contain multiple paragraphs. Add a `>` on the blank lines between the paragraphs.

Blockquotes can contain other [markdown](markdown.md) formatted elements. Not all elements can be used.

It is good practice to put a blank line above and below a heading for compatibility.

**Syntax:**
```md
> It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.
>
>> Time will not slow down when something unpleasant lies ahead.
> 
> ### Heading in blockquotes
> 
> **Bold in blockquotes**
> 
> *Italic in blockquotes* 
> 
> - Unordered list item 1 in blockquotes
> - Unordered list item 2 in blockquotes
>   - Nested unordered list item in blockquotes
> 
> 1. Ordered list item 1 in blockquotes
> 2. Ordered list item 2 in blockquotes 
> 
> If you want to know what a man’s like, take a good look at how he treats his inferiors, not his equals.
```

**Output:**

> It takes a great deal of bravery to stand up to our enemies, but just as much to stand up to our friends.
>
>> Time will not slow down when something unpleasant lies ahead.
> 
> ### Heading in blockquotes
> 
> **Bold in blockquotes**
> 
> *Italic in blockquotes* 
> 
> - Unordered list item 1 in blockquotes
> - Unordered list item 2 in blockquotes
>   - Nested unordered list item in blockquotes
> 
> 1. Ordered list item 1 in blockquotes
> 2. Ordered list item 2 in blockquotes 
> 
> If you want to know what a man’s like, take a good look at how he treats his inferiors, not his equals.

---