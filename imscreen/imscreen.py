import mss
import numpy
import cv2
import time
import math
import pyautogui

scr_width, scr_height = pyautogui.size()
vs = cv2.VideoCapture(0)
global st
st = 0
def capture(y=0,x=0,w=int(scr_width),h=int(scr_height)):

    if not type(y) == str:
        w = w-y
        h = h-x
    global st
    st = time.time()
    try:
        if type(y) == str:
            success,frame = vs.read(0)
            return (True,frame)
        else:
            assert w != 0, '>> Error! Width Cannot be Zero.'
            assert h != 0, '>> Error! Height Cannot be Zero.'
            with mss.mss() as sct:
                monitor = {"top": x, "left": y, "width": w, "height": h}
                img = cv2.cvtColor(numpy.array(sct.grab(monitor)),cv2.COLOR_BGRA2BGR)
                return (True,img)
    except Exception as e:
        print(e)
        return (False,bin)

global fps_dict
fps_dict = {0:30, 1:30, 2:30, 3:30, 4:30, 5:30, 6:30 ,7:30 ,8:30 ,9:30 ,10:30 ,11:30 ,12:30 ,13:30 ,14:30 ,15:30}

global fps_idx
fps_idx = 0
def fps(log = False):
    try:
        global st
        global fps_dict
        global fps_idx

        if fps_idx == len(list(fps_dict.values())):
            fps_idx = 0

        et = time.time()
        tt = 1/(et-st)
        FPS = round(tt)
        FPS = int(math.ceil(FPS / 10.0)) * 10

        fps_dict.update({fps_idx:FPS})
        average_fps = max(list(fps_dict.values()))
        fps_idx +=1
        return average_fps
    except:
        FPS = 0
        fps_dict = {0:30, 1:30, 2:30, 3:30, 4:30, 5:30}
        fps_idx = 0
        return FPS
    finally:
        if log == True:
            print('FPS: {}'.format(average_fps))


