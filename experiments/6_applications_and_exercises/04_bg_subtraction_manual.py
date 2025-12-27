import cv2
import numpy as np

path = "C:\\Users\\Dimoontri\\Desktop\\python_and__Libraries\\opencv_udemy\\08_Exercises\\sources\\car.mp4"

cap = cv2.VideoCapture(path)
ret, first_frame = cap.read()
first_frame = cv2.resize(first_frame,(640,480))
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray,(5,5),0)


while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),0)

    diff = cv2.absdiff(first_gray,gray)
    ret, diff = cv2.threshold(diff,50,255,cv2.THRESH_BINARY)

    cv2.imshow("frame",frame)
    cv2.imshow("first_frame",first_frame)
    cv2.imshow("diff",diff)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()