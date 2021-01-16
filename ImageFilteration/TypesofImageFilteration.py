#Better Output Result
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("Images/images (5).jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  #GRAYSCORE IMAGE

kernel = np.ones((5,5), np.float32)/25  # We can go anynumber above 25. below 25 it gives bad output

convo = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gblur = cv.GaussianBlur(img, (5, 5), 0)
mblur = cv.medianBlur(img,5)
bifil = cv.bilateralFilter(img, 9, 75, 75)

titles = ["Original Image", "2D Convolution", "Blur", "Gaussian Blur", "Median Blur", "Bilateral Filter"]

images = [img, convo, blur, gblur, mblur, bifil]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()