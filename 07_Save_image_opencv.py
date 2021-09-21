# (07)******************save images using openCV in python***************

# if we want to save the images than we use this method

# ---importing libraries
import numpy as np
import cv2
import os

# ---genratting the values 0 to 255 using numpy library
rand_array = np.random.randint(255, size=(300,600,3))
# print(rand_array)
# ---to save the image we use imwrite function 
# cv2.imwrite('array_image.JPEG',rand_array)

# ----for reading the image we use imread function
# img=cv2.imread('array_image.JPEG',)

# ----showing the image 
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -----if we want to save te images which we read it than we use this function
# img_path = 'images/IMG_4780.JPG'
# img=cv2.imread(img_path)
# img = cv2.resize(img,(1000,800))
# cv2.imshow('image',img)

# ----for saving the image we use imwrite function
# cv2.imwrite('img_converter.png',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -----if we want to save images from videos we use this method
video_path = r'D:\\machine learning practice\\openCV\\Amazon shopping cart demo at Amazon Fresh grocery store Woodland Hills(720P_HD).mp4'

# ---for creating the directory
os.mkdir('video_to_image')

# ---for capture the video
cap = cv2.VideoCapture(video_path)

img_count=1
while cap.isOpened():
    # ---this is for reading the video
    ret,frame = cap.read()
    frame = cv2.resize(frame,(600,400))
    if not ret:
        print("Unable to read frame")
        break
    # ----for saving the images from video 
    is_img_write = cv2.imwrite(f"video_to_image\image{img_count}.jpeg",frame)
    if is_img_write:
        print(f"image save at video_to_image\image{img_count}.jpeg")
    cv2.imshow('video',frame)
    cv2.waitKey(25) & 0xff==ord('q')
    img_count +=1
cap.release()
cv2.destroyAllWindows()


