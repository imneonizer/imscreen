# imscreen
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
#### About
This is the Official Github Repository for PyPI package `imscreen`.
imscreen is intended to provide seamless functions for quickly capturing frames from `webcam / computer's screen` with Ultra High Frame Rates.

> Quickly and efficiently capture screen / webcam with no hassle, the captured frame is returned as Numpy N-dimensional Array, So are very easy to read and process with OpenCV. On an average powered computer, it was able to capture frames with `80 FPS`

### External Modules Used Inside the Package
```
>> opencv-contrib-python
>> numpy
>> mss
>> screeninfo
```
### Usage
```
import imscreen
import cv2
while True:
    success, frame = imscreen.capture(0,0,100,100)
    if not success:
        break
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
```

### Functions Overview
```
success, frame = imscreen.capture(0,0,100,100)
```
The function `imscreen.capture()` takes four positional arguments which are nothing but `Top, Left, Width, Height` Coordinates of the screen which are required to capture. And returns a Boolean, Frame. The Boolean is used to check if there is any error in reading the frames so that wea can `break` loops while capturing continuously.
>> Note:- Capturing only required area of screen results in Higher FPS.

##### Let's see what else we can do with the `capture()` function
If we pass only two values to the function, the other two arguments will be set as screen's resolution width and height by default.
`imscreen.capture(10,100)` will be treated as `imscreen.capture(10,100,screen_width, screen_height)`

If we don't pass any values to the function, it will capture the whole screen by default.
`imscreen.capture()` will be treated as `imscreen.capture(0,0,screen_width,screen_height)`

Atlast, if we pass any string value to the function, say: '0', it will capture frames from your default webcam.
`imscreen.capture('0')` will be treated as `imscreen.capture(webcam)`

##### This library also provides FPS with / without logging in the console.
```
fps = imscreen.fps(log = True)
```

`imscreen.fps()` returns FPS and if we set `fps(log = True)` it will also print out in the console, and if we set `fps = imscreen.fps(log = False)`, this means the fps will be stored inside the `fps` variable but will not print the FPS inisde the console, this can be preety handy when you only want to see the FPS in the console or if you need to store it inside some variable, so that later it can be used to write on to the frame directly.

#### Example
```
import cv2
import numpy as np
import imscreen

while True:
    success, frame = imscreen.capture(0,0,100,100)
    if not success:
        break
    fps = imscreen.fps(log = True)
    cv2.putText(frame, "FPS: {}".format(fps), (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
```

Hope you enjoyed today's tutorial. Don't forget to star the repository.
if you have any query, feel free to ask.

twitter `@imneonizer`

insta `@the.nitin.rai`

gmail `mneonizer@gmail.com`
