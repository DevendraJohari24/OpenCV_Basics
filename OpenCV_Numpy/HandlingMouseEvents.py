import numpy as np
import cv2 as cv
#Below code is help to show events
#events = [i for i in dir(cv) if "EVENT" in i]
#print(events)   #PRINTS SO MANY EVENTS FOR WHAT WE DO WITH MOUSE OR KEYBOARD

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, ",", y)
        font = cv.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + "," + str(y)
        cv.putText(img, strXY, (x, y), font, 1 , (0, 0 , 255), 2)
        cv.imshow("Image", img)

#img = np.zeros([512, 512, 3], np.uint8)
img = cv.imread("image.jpg")
cv.imshow("Image", img)
cv.setMouseCallback("Image", click_event)

cv.waitKey(0)
cv.destroyAllWindows()