import  cv2 as cv

import numpy as np

img1 = cv.imread("Images/photo_2021-01-16_10-33-54.jpg")
img2 = cv.imread("Images/images (13).jpg")

img1 = cv.resize(img1, (600,600))
img2 = cv.resize(img2, (600,600))
print(img1.shape)
print(img2.shape)

result_horizontal = np.hstack((img1[:, :300], img2[:,300:]))
result = np.hstack((img1[:, :600], img2[:,0:]))
result_vertical = np.vstack((img1[:300,:],img2[300:,:]))

print(result.shape)
print(result_vertical.shape)
print(result_horizontal.shape)

cv.imshow("Apple", img1)
cv.imshow("Orange", img2)
cv.imshow("Result", result)
cv.imshow("Result Horizontal", result_horizontal)
cv.imshow("Result Vertical", result_vertical)

cv.waitKey(0)
cv.destroyAllWindows()