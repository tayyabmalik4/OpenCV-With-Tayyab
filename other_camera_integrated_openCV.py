# ----first of all importing libraries
import numpy as np
import cv2

# ---To run the Camera we use vedioCapture function
cap = cv2.VideoCapture(0)

# ---url of the camera
url ='https://192.168.0.103:8080/video'
# ---Now we integrated the camera and url
cap.open(url)

# ----Now we open the while loop to run the code
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        resize=cv2.resize(frame,(600,400))
        cv2.imshow("Boom guys",resize)
        if cv2.waitKey(25) & 0xff==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()