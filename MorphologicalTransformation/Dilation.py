import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Images/Color-Balls-2.jpg", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)

dilation = cv.dilate(mask, kernal, iterations=10)

title = ["Image", "Mask", "Dilation"]
images = [img, mask, dilation]

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], "gray")
    plt.title([title[i]])
    plt.xticks([])
    plt.yticks([])

plt.show()
