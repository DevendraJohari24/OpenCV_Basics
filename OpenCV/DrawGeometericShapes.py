import cv2 as cv

img = cv.imread("image.jpg" , 1)

#DRAW A LINE
img = cv.line(img, (0,0) , (255, 145), (255,0,0), thickness=20)
img = cv.arrowedLine(img, (0,512) , (255, 145), (0,255,0), thickness=10)
cv.imshow("Image", img)

#DRAW A RECTANGLE
img1 = cv.imread("image1.jpg" , 1)
img1 = cv.rectangle(img1, (100,355),(255,505), (0,0,255),thickness=7)
#FILL A RECTANGLE
img1 = cv.rectangle(img1, (100,355),(255,505), (0,255,0),-1)

cv.imshow("Rectangle", img1)

#DRAW A CIRCLE
img2 = cv.imread("imagetest (2).jpg" , 1)
img2 = cv.circle(img2, (255,255), 100, (0,0,255), thickness=7)

#Fill the circle
img2 = cv.circle(img2, (255,255), 100, (0,255,0), -1)


cv.imshow("Circle", img2)
cv.waitKey(0)
cv.destroyAllWindows()