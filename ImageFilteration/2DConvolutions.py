#Better Output Result
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Images/images (2).jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  #GRAYSCORE IMAGE

kernel = np.ones((5,5), np.float32)/25  # We can go anynumber above 25. below 25 it gives bad output

convo = cv.filter2D(img, -1, kernel)

titles = ["Original Image", "2D Convolution"]

images = [img, convo]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()