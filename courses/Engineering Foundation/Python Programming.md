# Python Programming

> Vidath Dissanayake | Sri Lanka  
> Tags: #courses #courses/PreEng #programming/python  
> Links: [Engineering Foundation](Engineering%20Foundation.md) [Python](../../programming/python/Python.md)
> Sources:  

---

## 1. Turtle Graphics

> Links:  
> Sources: [Python 1 - Turtle Graphics (English)](https://www.youtube.com/watch?v=Hu6ERdNJpOA) [Trinket](https://trinket.io/turtle)

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


