import mss
import numpy
import cv2
import time
import math
from screeninfo import get_monitors
scr_width, scr_height = str(get_monitors()[0]).split('(')[1].split('+')[0].split('x')
vs = cv2.VideoCapture(0)
global st
st = 0
def capture(y=0,x=0,w=int(scr_width),h=int(scr_width)):
    w = w-y
    h = h-x
    global st
    st = time.time()
    try:
        if type(x) == type(''):
            success,frame = vs.read()
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

def fps(log = False):
    try:
        global st
        et = time.time()
        tt = 1/(et-st)
        FPS = round(tt)
        FPS = int(math.ceil(FPS / 10.0)) * 10
        if log == True:
            print('FPS: {}'.format(FPS))
        return FPS
    except:
        if log == True:
            print('FPS: {}'.format(0))
        return 0


