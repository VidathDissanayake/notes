# Code and Horizontal lines

Code and Horizontal line syntax in [Markdown](markdown/Markdown.md)

## Code

To add code inline, surround the code with `backticks` (`` ` ``).

To create code blocks, indent every line of the block by at least `4 spaces` or `1 tab`.

To create fenced code blocks, use `3 backticks` (` ``` `) or `3 tildes` (`~~~`) on the lines before and after the code block.  
To add syntax highlighting, specify a language next to the backticks before the fenced code block.

**Syntax:**

````md
Type `msfconsole` in the terminal and press enter.

    This is the first line of code block
    This is the second line of code block
    This is the third line of code block

```md

# This is a markdown heading

**This is bold text in markdown**

*This is italic text in markdown*
```
````

**Output:**

Type `msfconsole` in the terminal and press enter.

    This is the first line of code block
    This is the second line of code block
    This is the third line of code block

```md

# This is a markdown heading

**This is bold text in markdown**

*This is italic text in markdown*
```

---

## Horizontal Line

To create a horizontal rule, use three or more `asterisks` (`***`), `dashes` (`---`), or `underscores` (`___`) on a line by themselves.

For compatibility, put blank lines before and after horizontal rules.

**Syntax:**

```md
---

***

___
```

**Output:**

---

***

___