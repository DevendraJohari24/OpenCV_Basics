import cv2 as cv


img = cv.imread("image.jpg", 1)

cv.imshow("Image", img)

e = cv.waitKey()

if e == 27:
    cv.destroyAllWindows()

elif e == ord("s"):
    cv.imwrite("image_new.jpg", img)
    cv.destroyAllWindows()

