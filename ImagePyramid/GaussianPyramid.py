#WOrk with different resolutions of image These set of different resolutions of a image is called Image Pyramid

import cv2 as cv

img = cv.imread("Images/photo_2021-01-16_10-29-50.jpg")
scale_percent = 60  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)


lower_resolution = cv.pyrDown(img)
lower_resolution_1 = cv.pyrDown(lower_resolution)
lower_resolution_2 = cv.pyrDown(lower_resolution_1)
lower_resolution_3 = cv.pyrDown(lower_resolution_2)
lower_resolution_4 = cv.pyrDown(lower_resolution_3)
higher_resolution = cv.pyrUp(lower_resolution_2)

cv.imshow("Image", img)
cv.imshow("PyrDown Image", lower_resolution)
cv.imshow("PyrDown 1 Image", lower_resolution_1)
cv.imshow("PyrDown 2 Image", lower_resolution_2)
cv.imshow("PyrDown 3 Image", lower_resolution_3)
cv.imshow("PyrDown 4 Image", lower_resolution_4)
cv.imshow("PyrUp Image", higher_resolution)

cv.waitKey(0)
cv.destroyAllWindows()