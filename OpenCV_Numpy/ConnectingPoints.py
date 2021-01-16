import numpy as np
import cv2 as cv

def click_event(event, x ,y , flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x, y), 10, (0, 0, 255), 1)
        points.append((x,y))
        if len(points) >= 2:
            cv.line(img, points[-1], points[-2], (0,255,0), 5)

        cv.imshow("Image", img)



points = [ ]
#img =  np.zeros((500, 500, 3), np.uint8)
img = cv.imread("image3.jpg")
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
