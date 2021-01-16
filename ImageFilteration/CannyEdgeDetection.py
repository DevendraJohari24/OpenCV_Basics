import  cv2 as cv
from matplotlib import  pyplot as plt

img = cv.imread("Images/images (9).jpg",0)

canny = cv.Canny(img, 50, 150)  #this third parameter helps to increase or decrease the noise

titles = ["Image", "Canny"]
images = [img, canny]

for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()