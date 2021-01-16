import cv2 as cv
#Read an image
img  = cv.imread("image1.jpg" , 0)   # 1 for Colored Image(RGB Three Channels) ..... 0 for Gray Image(White Channel)
print(img)

#Show an Image
cv.imshow("Image", img)

#Create a New Image
cv.imwrite("image_create.jpg", img)



cv.waitKey(delay=5000)
cv.destroyWindow()