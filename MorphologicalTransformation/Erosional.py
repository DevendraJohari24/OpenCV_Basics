#USEFUL IN REMOVING WHITE NOISE
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Images/Color-Balls-2.jpg", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((2,2), np.uint8)

dilation = cv.dilate(mask, kernal, iterations=10)  #MORE ITERATION MORE IT COVERS BLACK SPACES
erosion = cv.erode(mask, kernal, iterations=10)  #MORE ITERATION MORE IT COVERS BLACK SPACES

title = ["Image", "Mask", "Dilation", "Erosion"]
images = [img, mask, dilation, erosion]

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], "gray")
    plt.title([title[i]])
    plt.xticks([])
    plt.yticks([])

plt.show()
