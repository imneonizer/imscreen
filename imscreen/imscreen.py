import mss
import numpy
import cv2
import time
import math
import pyautogui

FPS = 0
counter = 0
st = time.time()

scr_width, scr_height = pyautogui.size()
vs = cv2.VideoCapture(0)

def capture(y=0,x=0,w=int(scr_width),h=int(scr_height)):

    if not type(y) == str:
        w = w-y
        h = h-x

    try:
        if type(y) == str:
            success,frame = vs.read(0)
            return (True, frame)
        else:
            assert w != 0, '>> Error! Width Cannot be Zero.'
            assert h != 0, '>> Error! Height Cannot be Zero.'
            with mss.mss() as sct:
                monitor = {"top": x, "left": y, "width": w, "height": h}
                img = cv2.cvtColor(numpy.array(sct.grab(monitor)),cv2.COLOR_BGRA2BGR)
                return (True, img)
    except Exception as e:
        print(e)
        return (False, bin)

def fps(log = False):
    global FPS
    global counter
    global st
    
    counter+=1
    if (time.time() - st) > 1 :
        FPS = round(counter / (time.time() - st))
        counter = 0
        st = time.time()

    if log == True:
            print('FPS: {}'.format(FPS))

    return FPS

