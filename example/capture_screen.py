import cv2
import imscreen

while True:
    success, frame = imscreen.capture(0,0,400,300)
    if not success:
        break

    fps = imscreen.fps(log = True)
    cv2.putText(frame, "FPS: {}".format(fps), (0, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
    cv2.imwrite('screen_shot.png',frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == ord('q'):
        break
