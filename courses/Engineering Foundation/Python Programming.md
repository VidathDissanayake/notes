# Python Programming

> Vidath Dissanayake | Sri Lanka  
> Tags: #courses #courses/PreEng #programming/python  
> Links: [Engineering Foundation](Engineering%20Foundation.md) [Python](../../programming/python/Python.md)
> Sources:  

---

## 1. Turtle Graphics

> Links:  
> Sources: [Python 1 - Turtle Graphics (English)](https://www.youtube.com/watch?v=Hu6ERdNJpOA) [Trinket](https://trinket.io/turtle)

![Day_01_Turtle_Graphics_Online](assets/documents/Day_01_Turtle_Graphics_Online.pdf)

Turtle graphics is a popular way for introducing programming to beginners.
We can use the online interpreter [Trinket](https://trinket.io/turtle) for this.

First, you should import the “turtle” module.
```python
from turtle import *
```

Available functions for Turtle:
- `forward/fd(pixels)` - Move forward
- `backward/back/bw(pixels)` - Move backwards
- `left(degrees)` - Turn left
- `right(degrees)` - Turn right
- `home()` - Return to the origin along the shortest path.
- `clear()` - Clear the screen.
- `reset()` - Clear the screen and set position to origin/home.
- `penup()` and `pendown()` - Anything between these 2 functions are not drawn.
- `setpos(x,y)` - Moves the turtle head to the given coordinate along the shortest path. No change to the direction the dead is facing.
- `setx(x)` - Similar to `setpos()`. Only changes the x coordinate.
- `sety(y)` - Similar to `setpos()`. Only changes the y coordinate.
- `setheading(anticlockwise angle)` - Directly sets the heading irrespective of previous direction facing.
- `speed(0-9)` - `1` is the slowest. Speed increases with integer. `0` is considered `10` and is the fastest.
- `stamp()` - Leaves a copy of the turtle head in the current position.
- `circle(radius,arc_angle)` - Draws a circle starting from the current position and using the current direction as a tangent.
- `dot(pixels)` - Places a dot with the current position of the turtle as centre and the diameter of the pixels specified.
- `pencolor(colour)` - Changes the colour of the lines drawn to the colour specified.
- `fillcolor(colour)` - Used in conjunction with `begin_fill()` and `end_fill()`. Fills whatever is between these two functions in the colour specified.
- `ht()` - Hides the turtle head.
- `st()` - Shows the turtle head again after being hidden by `ht()`.
- `write()` - Writes text on the screen at the current turtle head position. You can format the text using, 
```python
write('{text}', align='{alignment}', font=('{font}', {size}, '{modifiers(bold/italic)}')```

You can you normal python operations such as loops, `input()` and comparisons. x

You can also provide mathematical expressions as the input for functions.
E.g:
```python
forward(50+50)
left(45*2)
backward(100*2**0.5)
```

You can write multiple commands in the same line using semi-colons (`;`).
E.g:
```python
left(90); forward(100; forward(50)
```
---


## 2. Python IDLE as a Calculator


> Links:  [3. Python Programming – Basics](../UoM/Python%20for%20Beginners/3.%20Python%20Programming%20–%20Basics.md)
> Sources: [Python 2 English Python IDLE as a Calculator](https://www.youtube.com/watch?v=hul3niTcHBY) [Download Python](https://www.python.org/downloads/?authuser=0) [Download QPython for Mobile](https://play.google.com/store/apps/details?id=org.qpython.qpy3&hl=en&gl=US&pli=1)

![Day_02_Getting started](assets/documents/Day_02_Getting%20started.pdf)

An Integrated Development Environment (IDE) is useful when programming. Python comes with an IDE called IDLE. 

For details about arithmetic operations, refer to [3. Python Programming – Basics](../UoM/Python%20for%20Beginners/3.%20Python%20Programming%20–%20Basics.md).

You can use `e` to denote `*10**` for numbers.
E.g:
- `1e3` = 1000
- `1e-3` = 0.001

When using mathematical functions, it should be kept in mind that some numbers are not exactly represented in binary and therefore functions can give unexpected results. 
E.g:
- `round(3.5)` = 4
- `round(4.5)` = 4
- `round(5.5)` = 6
- `math.sin(math.pi/2)` = 1.0
- `math.cos(math.pi/2)` = 6.123233995736766e-17


`round({float},{no of decimal places})` can be used to round off floats. Default behaviour is to round to an integer.

For more advanced mathematical functions, you can import the math library by `import math`. This allows you to use functions like trigonometric functions and constants such as pi.

When importing libraries, there are several ways to do it.
- `import library` - Imports the entire library. Can access functions by using `library.function()`
- `from library import *` - Imports the entire library. Can access functions by directly using `function()`.
- `from library import function` - Imports only the necessary function. Can access function by directly using `function()`.
- `from library import function as f` - Imports only the necessary function. Can access function by directly using `f()`.

---

## Variables and Comments

> Links: [3. Python Programming – Basics](../UoM/Python%20for%20Beginners/3.%20Python%20Programming%20–%20Basics.md)
> Sources: [Python 3 - Variables and Comments ( Mixed -2021)](https://www.youtube.com/watch?v=88s4hjWf_lE)

In python, anything after a `#` is considered as a comment.

For more about variables, refer to [3. Python Programming – Basics](../UoM/Python%20for%20Beginners/3.%20Python%20Programming%20–%20Basics.md).

A variable can be deleted using `del variable`.