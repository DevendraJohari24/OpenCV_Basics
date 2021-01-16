import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread("Images/images (3).jpg", -1)
cv.imshow("Images", img)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)
plt.xticks([]), plt.yticks([]) #USED TO REMOVING AXISES

plt.show()