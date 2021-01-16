import numpy as np
import cv2 as cv

def display():
    pass

cv.namedWindow("HSV Tracker")
cv.createTrackbar("LH", "HSV Tracker", 0, 255, display)
cv.createTrackbar("LS", "HSV Tracker", 0, 255, display)
cv.createTrackbar("LV", "HSV Tracker", 0, 255, display)
cv.createTrackbar("UH", "HSV Tracker", 255, 255, display)
cv.createTrackbar("US", "HSV Tracker", 255, 255, display)
cv.createTrackbar("UV", "HSV Tracker", 255, 255, display)

while True:
    img = cv.imread("Color-Balls-2.jpg")

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LH", "HSV Tracker")
    l_s = cv.getTrackbarPos("LS", "HSV Tracker")
    l_v = cv.getTrackbarPos("LV", "HSV Tracker")

    u_h = cv.getTrackbarPos("UH", "HSV Tracker")
    u_s = cv.getTrackbarPos("US", "HSV Tracker")
    u_v = cv.getTrackbarPos("UV", "HSV Tracker")

    lower_hsv = np.array([l_h, l_s, l_v])
    upper_hsv = np.array([u_h, u_s, u_v])

    mask_hsv = cv.inRange(hsv, lower_hsv, upper_hsv)

    output_mask = cv.bitwise_and(img, img, mask=mask_hsv)

    cv.imshow("Image", img)
    cv.imshow("Mask", mask_hsv)
    cv.imshow("Output", output_mask)

    key = cv.waitKey(1)
    if key == 27:
        break

cv.destroyAllWindows()