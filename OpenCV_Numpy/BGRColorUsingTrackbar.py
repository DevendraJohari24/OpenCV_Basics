import numpy as np
import cv2 as cv
def display(x):
    print(x)


img = np.zeros((200, 250, 3), np.uint8)
cv.namedWindow("BGR Trackbar")


cv.createTrackbar("B", "BGR Trackbar", 0 , 255, display) #CREATING TRACKBAR
cv.createTrackbar("G", "BGR Trackbar", 0 , 255, display) #CREATING TRACKBAR
cv.createTrackbar("R", "BGR Trackbar", 0 , 255, display) #CREATING TRACKBAR
switch = "0:OFF \n 1:ON"
cv.createTrackbar(switch , "BGR Trackbar", 0, 1, display)

while(1):
    cv.imshow("BGR Trackbar", img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    B = cv.getTrackbarPos("B", "BGR Trackbar")
    G = cv.getTrackbarPos("G", "BGR Trackbar")
    R = cv.getTrackbarPos("R", "BGR Trackbar")
    S = cv.getTrackbarPos(switch, "BGR Trackbar")

    if S == 0:
        img[:] = 0
    else:
        img[:] = [B, G, R]

cv.destroyAllWindows()