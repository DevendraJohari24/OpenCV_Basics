import cv2 as cv

img = cv.imread("Images/images (1).jpg")

repeat = img.copy()

gauspyramid = [repeat]

for i in range(8):
    repeat = cv.pyrDown(repeat)
    gauspyramid.append(repeat)
    cv.imshow(str(i), repeat)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()