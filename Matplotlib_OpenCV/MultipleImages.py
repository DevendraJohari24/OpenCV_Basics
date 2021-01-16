import cv2  as cv
from matplotlib import pyplot as plt

img = cv.imread("Images/Gradient.jpg")

_, th0 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY_INV)
_, th2 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC)
_, th3 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO)
_, th4 = cv.threshold(img, 50, 255, cv.THRESH_TOZERO_INV)

titles = ["Main Image", "Binary", "Binary-Inv", "Trunc", "ToZero", "ToZero-Inv"]
images = [img, th0, th1, th2, th3, th4]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()