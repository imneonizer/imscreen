import cv2
import numpy as np
import imscreen

while True:
    success, frame = imscreen.capture(0,0,100,100)
    if not success:
        break

    fps = imscreen.fps(log = True)
    cv2.putText(frame, "FPS: {}".format(fps), (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.imwrite('screen_shot.png',frame)
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
    input('>> Press Enter to Capture Next Frame')
