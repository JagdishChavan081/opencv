#write a opencv2 program to read, write, show videos from camera in OpenCv

import cv2
cap=cv2.VideoCapture(0)

#capture frame contineously
while(True):
    ret, frame=cap.read()
    gray = cv2.cvtColor(frame)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
#release capture variable
cap.release()
cv2.destroyAllWindows()