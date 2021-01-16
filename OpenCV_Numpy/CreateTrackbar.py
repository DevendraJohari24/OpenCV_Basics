import numpy as np
import cv2 as cv
def display(x):
    print(x)


cv.namedWindow("BGR Trackbar")


cv.createTrackbar("Image", "BGR Trackbar", 0 , 255, display) #CREATING TRACKBAR
switch = "Color/Gray"
cv.createTrackbar(switch , "BGR Trackbar", 0, 1, display)

while(1):
    img = cv.imread("image4.jpg")
    pos = cv.getTrackbarPos("Image", "BGR Trackbar")
    font =  cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (400, 300), font, 2 , (0, 0, 255), 4)


    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    S = cv.getTrackbarPos(switch, "BGR Trackbar")

    if S == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow("BGR Trackbar", img)
cv.destroyAllWindows()