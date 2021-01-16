import  cv2 as cv

eye_cascade = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

img = cv.imread("image1.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
eye_detect = eye_cascade.detectMultiScale(gray_img, 1.1, 4)


for (x ,y ,w ,h) in eye_detect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=4)

cv.imshow("Image", img)
cv.waitKey(0)
