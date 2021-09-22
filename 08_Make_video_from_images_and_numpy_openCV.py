# (08)********************How to make video from images and numpy array in openCV using python**************

# ----importing libraries
import numpy as np
import cv2
import os

# ----Creating variables of height, weight and channals which we use to creat a video and also numpy arrays
width = 1280
height = 720
channal = 3

# ----creat a variable of frames fps means frame per secend
fps=10
sec = 5

# ****************This code is creating a video through numpy arrays

# ----cv2.VideoWriter_fourcc(*'MP42')---- this is the function to creat a vedio and * means to get all the parameters and 'MP42' means 4 cores
# fourcc = cv2.VideoWriter_fourcc(*'MP42') 

# ----VideoWriter function is use to save the video and it is basically 4 parameters first is the name of file--secend is the type of video third is the frames-per-secend and forth is the width and height 
# video = cv2.VideoWriter('test.mp4',fourcc,float(fps),(width,height))

# ----Created for loop which is basically to genrate the values
# for frame_count in range(fps*sec):
#     img = np.random.randint(0,255,(height,width,channal),dtype=np.uint8) 
#     video.write(img)

# video.release()


# *******************This code is creating a vedio using images
fourcc=cv2.VideoWriter_fourcc(*'MP42')
video = cv2.VideoWriter('image_to_video.mp4',fourcc,float(fps),(width,height))

# ----creat a variable which shows the directry path
directry=r'D:\\machine learning practice\\openCV\\openCV Programming\\images'
img_list = os.listdir(directry)

for frame_count in range(fps*sec):
    img_name = np.random.choice(img_list)
    img_path = os.path.join(directry,img_name)
    img =cv2.imread(img_path)
    img_resize = cv2.resize(img,(width,height))
    video.write(img_resize)

# -----for showing the video
path = r'image_to_video.avi'
cap = cv2.VideoCapture(path)
while cap.isOpened():
    ret,frame = cap.read()
    if ret:
        img=cv2.imshow('image_to_video',frame)
        if cv2.waitKey(25) & 0xff ==ord('q'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()