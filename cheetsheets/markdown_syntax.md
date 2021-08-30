# Markdown Cheetsheet

---
## Headers

There are 6 types of headers. Headers start with a `#` and a `space`. Size of header decreases when the number of `#` s increases.

Syntax:

```markdown
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6
```

Output:
# Header 1
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6

---

## Text Formatting
- To make text italic, surround the text with `*` or `_`.
- To make text bold, surround the text with `**` or `__`.
- To make text highlighted, surround the text with `==`. (**Note supported everywhere**)
- To strikethough text, surround the text with `~~`.
- To put text in a blockquote, prepend with `>` and a `space`.
- To subscript text, surround text with `~`. (**Note supported everywhere**)
- To superscript text, surround text with `^`. (**Note supported everywhere**)
- Use `\` for line breaks

Syntax:
```markdown
*text* or _text_ \
**text** or __text__ \
==text== \
~~text~~

> text

~text~ \
^text^ \
text \ text
```

Output:

*text* or _text_ \
**text** or __text__ \
==text== \
~~text~~

> text

~text~ \
^text^ \
text \ text

---

## Lists

There are 3 types of lists
1. Unordered lists
2. Ordered lists
3. Check lists

- Unordered lists start with `-` or `*` or `+` and a `space`.
- Ordered lists start with `1.` and a `space`. 
- Incomplete check lists start with `- [ ]` and a `space`.
- Complete check lists start with `- [x]` and a `space`.

***Note: Any list can be nested by indenting with `4 spaces` or `1 tab`***

Syntax:

```markdown
- Unordered list 1 item 1
- Unordered list 1 item 2
- Unordered list 1 item 3

* Unordered list 2 item 1
* Unordered list 2 item 1
* Unordered list 2 item 1

+ Unordered list 3 item 1
+ Unordered list 3 item 1
+ Unordered list 3 item 1

1. Ordered list item 1
2. Ordered list item 2
3. Ordered list item 3

- [ ] Incomplete check lisit
- [x] Complete check list
```

Output:

- Unordered list 1 item 1
- Unordered list 1 item 2
- Unordered list 1 item 3

* Unordered list 2 item 1
* Unordered list 2 item 1
* Unordered list 2 item 1

+ Unordered list 3 item 1
+ Unordered list 3 item 1
+ Unordered list 3 item 1

1. Ordered list item 1
2. Ordered list item 2
3. Ordered list item 3

- [ ] Incomplete check lisit
- [x] Complete check list

---