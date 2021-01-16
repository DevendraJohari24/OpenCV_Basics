import numpy as np
import cv2 as cv

#Numpy.zeros method return a new array of given shape and type filled with zeros

img = np.zeros([300,400,3], np.uint8)  #[shape(height, width) and channels]

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()