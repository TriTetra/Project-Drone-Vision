import cv2
import numpy as np

path = "C:\\Users\\Dimoontri\\Desktop\\python_and__Libraries\\opencv_udemy\\08_Exercises\\sources\\eye_motion.mp4"

cap = cv2.VideoCapture(path)

while 1:
    ret,frame = cap.read()
    if ret is False:
        break

    roi = frame[80:230,230:450]
    row, cols,_ = roi.shape

    gray =cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    _,treshold = cv2.threshold(gray,2,255,cv2.THRESH_BINARY_INV)

    countors,_ = cv2.findContours(treshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    countors = sorted(countors, key = lambda x: cv2.contourArea(x), reverse=True)

    for cnt in countors:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.line(roi,(x+int(w/2),0),(x+int(w/2),row),(0,255,0),2)
        cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
        break


    cv2.imshow("roi",roi)
    cv2.imshow("Treshold",treshold)
    cv2.imshow("frame",frame)

    if cv2.waitKey(80) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()