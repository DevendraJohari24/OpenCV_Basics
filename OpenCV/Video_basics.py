import cv2 as cv

#Read Video

#cap = cv.VideoCapture(0)  #WebCam
cap = cv.VideoCapture("road.mp4")   #Video Playing

#while(True):
#    ret, frame = cap.read()

#    cv.imshow("Frame", frame)

 #   if cv.waitKey(1) & 0xFF == ord("e"):
 #       break


#cap.release()
#cv.destroyAllWindows()

while (True):
    ret, frame = cap.read()

    gray_vid = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("Frame", gray_vid)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()

