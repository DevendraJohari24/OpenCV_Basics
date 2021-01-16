import cv2 as cv

#Technique of image processing that based on shapes and forms of images.
#applied an instruction element on input image and provide an output image of same size
#instruction element or Kernel
#Two operation based on this is Dilation and Erosion

from matplotlib import pyplot as plt

img = cv.imread("Images/Color-Balls-2.jpg", 0)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY)
title = ["Image", "Mask"]
images = [img, mask]

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], "gray")
    plt.title([title[i]])
    plt.xticks([])
    plt.yticks([])

plt.show()
