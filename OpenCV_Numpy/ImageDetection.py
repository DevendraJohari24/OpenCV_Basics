import numpy as np
import cv2 as cv

while (True):
    img = cv.imread("image4.jpg")
    #First to convert it into HSV image

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lower_blue = np.array([118, 33, 50])
    upper_blue = np.array([127, 255, 255])

    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

    output_Mask_Bit = cv.bitwise_and(img, img, mask=mask_blue)

    cv.imshow("Image", img)

    cv.imshow("Mask" , mask_blue)

    cv.imshow("Output", output_Mask_Bit)

    key = cv.waitKey(0)
    if key == 27:
        break

cv.destroyAllWindows()