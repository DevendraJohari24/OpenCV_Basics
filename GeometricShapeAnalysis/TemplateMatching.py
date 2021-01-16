import cv2 as cv

import  numpy as np

img = cv.imread("Images/Ronaldo-Ball.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_temp = cv.imread("Images/Ronaldo-Cut-7.jpg", 0)

w, h = img_temp.shape[::-1]

res_match = cv.matchTemplate(gray_img, img_temp, cv.TM_CCORR_NORMED)

print(res_match)
threshold = 0.99
pass_thresh = np.where(res_match >= threshold)
print(pass_thresh)

for temp_pt in zip(*pass_thresh[::-1]):
    cv.rectangle(img, temp_pt, (temp_pt[0]+w, temp_pt[1]+h), (255,0,0), 2)

cv.imshow("Image", img)

cv.waitKey(0)
cv.destroyAllWindows()