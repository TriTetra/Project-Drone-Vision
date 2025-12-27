import cv2
import numpy as np

path = "C:\\Users\\Dimoontri\\Desktop\\python_and__Libraries\\opencv_udemy\\08_Exercises\\sources\\car.mp4"
cap = cv2.VideoCapture(path)
subtractor = cv2.createBackgroundSubtractorMOG2(history =100,varThreshold=120,detectShadows=True)


while 1:
    ret, frame = cap.read()
    frame = cv2.resize(frame,(640,480))
    mask = subtractor.apply(frame)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()