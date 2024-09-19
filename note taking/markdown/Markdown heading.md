# Headings

> Vidath Dissanayake | Sri Lanka  
> Tags: #markdown  
> Links: [markdown](markdown.md)  
> Sources:  

Heading syntax in [markdown](markdown.md).

There are 6 levels of headings. Headings start with a `#` and a `space`. Size of heading decreases when the number of `#` s increases.

Alternatively adding any number of `=` on the line below will convert the line above to `Heading level 1` and adding any number of `-` on the line below will convert the line above to `Heading level 2`

It is good practice to put a blank line above and below a heading for compatibility.

Heading ID can be specified with `#custom-id}` at the end of the heading.

**Syntax:**

```md
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

### Heading with custom ID {#My custom ID}
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

### Heading with custom ID {#My-custom-ID}

---