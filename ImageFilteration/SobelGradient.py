import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Images/Calendar-2.jpg")

sobelX = cv.Sobel(img, cv.CV_64F, 1 ,0 , ksize=1)
sobelY = cv.Sobel(img, cv.CV_64F, 0 , 1, ksize=1)

sobelXY = cv.bitwise_or(sobelX, sobelY)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
titles = ["Image", "SobelX", "SobelY", "SobelXY"]
images = [img, sobelX, sobelY, sobelXY]

for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
