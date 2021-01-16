import cv2 as cv

img = cv.imread("Images/Ronaldo-3.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

new, thresh = cv.threshold(gray, 127, 255, 0)

contours, hieraechy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

print("Contours Number = " + str(len(contours)))

print(contours[0])

cv.drawContours(img, contours, -1, (0, 255, 0), 2)

cv.imshow("Image", img)
cv.imshow("Gray Image", gray)

cv.waitKey(0)
cv.destroyAllWindows()