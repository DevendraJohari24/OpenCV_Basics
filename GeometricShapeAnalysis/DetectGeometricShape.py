import cv2 as cv

img = cv.imread("Images/Shape.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(gray, 230, 255, cv.THRESH_BINARY)

cv.imshow("Original Image", img)

contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour  in contours:
    approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, True), True)
    cv.drawContours(img, [approx], -1, (0, 255, 0), 2)

cv.imshow("Shapes", img)
cv.waitKey(0)
cv.destroyAllWindows()