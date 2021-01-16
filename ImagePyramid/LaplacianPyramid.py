import cv2 as cv

img = cv.imread("Images/apple.jpg")

repeat = img.copy()
gauspy = [repeat]

for i in range(6):
    repeat = cv.pyrDown(repeat)
    gauspy.append(repeat)

repeat = gauspy[5]
cv.imshow("Upper Level", repeat)

rep = [repeat]

for i in range(5, 0, -1):
    #CREATE EXPANDED VERSION OF UPPER LEVEL IN GAUSSIAN PYRAMID
    gaussian_expanded = cv.pyrUp(gauspy[i])
    laplacian = cv.subtract(gauspy[i-1], gaussian_expanded)
    cv.imshow(str(i), laplacian)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()
