# (04)*****************Play vedios and also integrated cameras*****************

# ---Discuss About----
# ---Play vedios
# ---Integrated Cameras
# ---Multile vedios/camera in one window

import numpy as np
import cv2

vedio_path = r'D:\\machine learning practice\\openCV\\Amazon shopping cart demo at Amazon Fresh grocery store Woodland Hills(720P_HD).mp4'
# cap = cv2.VideoCapture(0)
# url = 'https://192.168.0.103:8080/video'
# cap.open(url)
cap = cv2.VideoCapture(vedio_path)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        image = cv2.resize(frame,(600,400))
        cv2.imshow("play vedio",image)

        if cv2.waitKey(25) & 0xff==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()

# ----if we want to play multiple vedeos in one window than we use this method
# cap_camera = cv2.VideoCapture(0) 
# cap2 = cv2.VideoCapture(vedio_path) 
# while cap2.isOpened():
#     ret,frame = cap2.read()
#     ret2,frame2 = cap_camera.read()
#     if ret:
#         frame = cv2.resize(frame,(600,300))
#         camera_frame=cv2.resize(frame2,(600,300))
#         frame_2 = np.hstack((frame,frame))
#         frame_02 = np.hstack((camera_frame,camera_frame))
#         frame_4 = np.vstack((frame_2,frame_02))

#         cv2.imshow("Vedio player ", frame_4)
#         if cv2.waitKey(25) & 0xff==ord('q'):
#             break
#     else:
#         break
# cap2.release()
# cv2.destroyAllWindows()
