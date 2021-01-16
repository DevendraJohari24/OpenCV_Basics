import cv2 as cv

img = cv.imread("imagetest (5).jpg", 1)



font = cv.FONT_HERSHEY_SIMPLEX
img = cv.putText(img, "OpenCV", (500,255), font, 2.5, (0,255,255), 5, cv.LINE_AA)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()