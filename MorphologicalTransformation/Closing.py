#Perform by eroted then dilated a image ...EROSION + DILATION = CLOSING
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Images/image3.jpg", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)

dilation = cv.dilate(mask, kernal, iterations=10)  #MORE ITERATION MORE IT COVERS BLACK SPACES
erosion = cv.erode(mask, kernal, iterations=10)  #MORE ITERATION MORE IT COVERS BLACK SPACES
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal, iterations=10)

title = ["Image", "Mask", "Dilation", "Erosion", "OPENING", "CLOSING"]
images = [img, mask, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], "gray")
    plt.title([title[i]])
    plt.xticks([])
    plt.yticks([])

plt.show()
