#Image Thresholding - : process of dividing a image into segments like foreground and background or in pixels for example Bannerisation
#Convert grey code images into binary code images

import cv2 as cv

img = cv.imread("Images/Gradient.jpg")

#_, th0 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
#_, th0 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
#_, th0 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC)
_, th0 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)


cv.imshow("Image", img)
cv.imshow("NewImage", th0)

cv.waitKey(0)
cv.destroyAllWindows()