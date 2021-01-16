import  cv2 as cv


img1 = cv.imread("image3.jpg")
img1 = cv.resize(img1, (800, 800)) #RESIZE


img2 = cv.imread("image4.jpg")
img2 = cv.resize(img2, (800, 800))  #RESIZE

#output = cv.add(img1, img2)   #GIVES ERROR IF SIZE IS DIFFERENT OF BOTH IMAGES AND USED TO ADD TWO IMAGES

output = cv.addWeighted(img1, 1, img2, 0.3, 0)  #This function add a value of alpha with the source image for dealing with which image looks more brighter

cv.imshow("Image", output)
cv.waitKey(0)

cv.destroyAllWindows()