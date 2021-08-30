# Markdown Cheetsheet

Refer [Markdown Guide](https://www.markdownguide.org/ "Markdown Guide")

---

## Headings

There are 6 levels of headings. Headings start with a `#` and a `space`. Size of heading decreases when the number of `#` s increases.

For heading level 1 

**Syntax:**

```markdown
# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6

Heading level 1
===============

Heading level 2
---------------
```

**Output:**

# Heading level 1

## Heading level 2

### Heading level 3

#### Heading level 4

##### Heading level 5

###### Heading level 6

Heading level 1
===============

Heading level 2
---------------

---

## Text Formatting
- To make text italic, surround the text with `*` or `_`.
- To make text bold, surround the text with `**` or `__`.
- To strikethough text, surround the text with `~~`.
- To put text in a blockquote, prepend with `>` and a `space`.
- Use `\` for line breaks

**Syntax:**

```markdown
*text* or _text_

**text** or __text__

~~text~~

> text

text \
text
```

**Output:**

*text* or _text_

**text** or __text__

~~text~~ 

> text

text \
text

---

## Lists

There are 3 types of lists
1. Unordered lists
2. Ordered lists
3. Task lists

- Unordered lists start with `-` or `*` or `+` and a `space`.
- Ordered lists start with `1.` and a `space`. 
- Incomplete task lists start with `- [ ]` and a `space`.
- Complete task lists start with `- [x]` and a `space`.

***Note: Any list can be nested by indenting with `4 spaces` or `1 tab`***

**Syntax:**

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

- [ ] Incomplete task lisit
- [x] Complete task list

- Layer 1
  - Layer 2
    - Layer 3
  - Layer 2
- Layer 1

1. Layer 1
   1. Layer 2
      1. Layer 3
   2. Layer 2
2. Layer 1

- [ ] Layer 1
  - [ ] Layer 2
    - [ ] Layer 3 
  - [ ] Layer 2
- [ ] Layer 1
```

**Output:**

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

- [ ] Incomplete task lisit
- [x] Complete task list

- Layer 1
  - Layer 2
    - Layer 3
  - Layer 2
- Layer 1

1. Layer 1
   1. Layer 2
      1. Layer 3
   2. Layer 2
2. Layer 1

- [ ] Layer 1
  - [ ] Layer 2
    - [ ] Layer 3 
  - [ ] Layer 2
- [ ] Layer 1

---

## Links

- Link syntax is `[Display Text](URL "Display text on mouse hover")`.
- Self links can also be used. The syntax is `[Display Text]()`.
- To add an image inline, the syntax is `![Alt Text](Image URL =resolution)`
- The URL can also be supplied in `square brackets [constant]`. The URL has to be defined as `[constant]: URL`

**Syntax:**

```markdown
```

**Output:**

