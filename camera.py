#write a opencv2 program to read, write, show videos from camera in OpenCv

import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc ,20.0 ,(640,480))


print(cap.isOpened())
#capture frame contineously
while(cap.isOpened()):
    ret, frame = cap.read()
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out.write(frame)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
#release capture variable
cap.release()
out.release()
cv2.destroyAllWindows()