#Adaptive Thresholding --: Mean and Gaussian Type
#add 0 to convert in grayscore image
import cv2 as cv

img = cv.imread("Images/Calendar-2.jpg", 0)
scale_percent = 60  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)

_, th1 = cv.threshold(img, 150, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

cv.imshow("Image", img)
cv.imshow("Binary Image", th1)
cv.imshow("Adaptive Mean Image", th2)
cv.imshow("Adaptive Gaussian Image", th3)
cv.waitKey(0)
cv.destroyAllWindows()