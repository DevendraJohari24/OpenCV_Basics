import numpy as np
import  cv2 as cv

def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        Blue = img[y, x, 0]
        Green = img[y, x, 1]
        Red = img[y, x, 2]
        ImageColor = np.zeros((300, 300, 3) , np.uint8)
        ImageColor[:] = [Blue, Green, Red]
        cv.imshow("BGR COLORS", ImageColor)

img = cv.imread("image1.jpg")
scale_percent = 60  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
cv.imshow("Image", img)

cv.setMouseCallback("Image", click_event)
cv.waitKey(0)
cv.destroyAllWindows()

