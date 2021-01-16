import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Images/images (7).jpg")

lap = cv.Laplacian(img, cv.CV_64F, ksize=1)

lap = np.uint8(np.absolute(lap))

titles = ["Image", "Laplacian Image"]
images = [img, lap]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
