# Lists

> Vidath Dissanayake | Sri Lanka  
> Tags: #markdown  
> Links: [markdown](markdown.md)  
> Sources:  

List syntax in [markdown](markdown.md).

There are 3 types of lists
1. Unordered lists
2. Ordered lists
3. Task lists

***Note: Any list can be nested by indenting with `4 spaces` or `1 tab`***

---

## Unordered Lists

> Links:  
> Sources:  

Unordered lists start with `dashes` (`-`), `asterisks` (`*`), or `plus signs` (`+`) and a `space`.

For compatibility, don’t mix and match delimiters (`-`,`+`,`*`) in the same list.

**Syntax:**

```md
- Unordered list 1 item 1
- Unordered list 1 item 2
- Unordered list 1 item 3

* Unordered list 2 item 1
* Unordered list 2 item 1
* Unordered list 2 item 1

+ Unordered list 3 item 1
+ Unordered list 3 item 1
+ Unordered list 3 item 1

- Layer 1
  - Layer 2
    - Layer 3
  - Layer 2
  1. Layer 2
     1. Layer 3
  2. Layer 2
  - [ ] Layer 2
    - [ ] Layer 3 
  - [ ] Layer 2
- Layer 1
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

- Layer 1
  - Layer 2
    - Layer 3
  - Layer 2
  1. Layer 2
     1. Layer 3
  2. Layer 2
  - [ ] Layer 2
    - [ ] Layer 3 
  - [ ] Layer 2
- Layer 1

---

## Ordered Lists

> Links:  
> Sources:  

Ordered lists start with `1.` and a `space`. 

Ordered list numbering will start with the given number and increment 1 for each list item.

The numbers don’t have to be in numerical order.

**Syntax:**

```md
1. Ordered list item 1
2. Ordered list item 2
3. Ordered list item 3

4. Layer 1
   - Layer 2
     - Layer 3
   - Layer 2
   1. Layer 2
      1. Layer 3
   2. Layer 2
   - [ ] Layer 2
     - [ ] Layer 3 
   - [ ] Layer 2
5. Layer 1
```

**Output:**

1. Ordered list item 1
2. Ordered list item 2
3. Ordered list item 3

4. Layer 1
   - Layer 2
     - Layer 3
   - Layer 2
   1. Layer 2
      1. Layer 3
   2. Layer 2
   - [ ] Layer 2
     - [ ] Layer 3 
   - [ ] Layer 2
5. Layer 1

---

## Task Lists

> Links:  
> Sources:  

Incomplete task lists start with `- [ ]` and a `space`.

Complete task lists start with `- [x]` and a `space`.

**Syntax:**

```md
- [ ] Incomplete task lisit
- [x] Complete task list

- [ ] Layer 1
  - Layer 2
    - Layer 3
  - Layer 2
  1. Layer 2
     1. Layer 3
  2. Layer 2
  - [ ] Layer 2
    - [ ] Layer 3 
  - [ ] Layer 2
- [ ] Layer 1
```

**Output:**

- [ ] Incomplete task lisit
- [x] Complete task list

- [ ] Layer 1
  - Layer 2
    - Layer 3
  - Layer 2
  1. Layer 2
     1. Layer 3
  2. Layer 2
  - [ ] Layer 2
    - [ ] Layer 3 
  - [ ] Layer 2
- [ ] Layer 1

---