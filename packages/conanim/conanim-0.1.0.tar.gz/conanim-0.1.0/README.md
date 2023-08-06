# conanim Library
**This python library is used for creating simple animations in console.**
## How to use

To create an animation you need use `frame_animattion()`function. Example:
```Python
import conanim as ca

# define frames for animation
frames = [
    "|",
    "/",
    "-",
    "\\",
]

while True:
    ca.frame_animation(frames, 0.1) # create an animation
```
In this example `frame_animation()` needs 2 arguments: frames and delay in seconds between frames
```Python 
frame_animation(frames, delay)
```
This is cool, but if we create program like this:
```Python
import conanim as ca

# define frames for animation
frames = [
    "|",
    "/",
    "-",
    "\\",
]

while True:
    print("loading ", end="")
    ca.frame_animation(frames, 0.1) # create an animation
```
it wil doesn't work, so this library have `print_with_animation()` function:
```Python
import conanim as ca

# define frames for animation
frames = [
    "|",
    "/",
    "-",
    "\\",
]

while True:
    ca.print_with_animation("Loading ", frames, 0.1) # create an animation
```
