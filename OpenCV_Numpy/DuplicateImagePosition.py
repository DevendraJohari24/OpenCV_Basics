import numpy as np
import  cv2 as cv

img = cv.imread("image1.jpg")
scale_percent = 60  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
#img = cv.rectangle(img, (300,300) , (500,500), (255,0,0),7)
#img = cv.rectangle(img, (0,0) , (200,200), (0,255,0),7)


#CONCEPT BEHIND DUPLICATING IS THIS-:
#THE COORDINATES USED IN THE ARRAY FOLLOW THE FORMAT OF IMAGE[y1:y2, x1:x2]
#THEREFORE WHEN COPYING TO ANOTHER PART OF THE IMAGE YOU NEED TO ENSURE THAT (y2-y1) VALUE REMAINS SAME, AS WELL AS (x2-x1)

myimg = img[300:500,300:500]  #COPY
img[0:200, 0:200] = myimg     #PASTE


cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()

