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
- `backward/back(pixels)` - Move backwards
- `left(degrees)` - Turn left
- `right(degrees)` - Turn right
- `home()` - Return to the origin along the shortest path.
- `clear()` - Clear the screen.
- `reset()` - Clear the screen and set position to origin/home.

You can also provide mathematical expressions as the input for functions.
E.g:
```python
forward(50+50)
left(45*2)
backward(100*2**0.5)
```

