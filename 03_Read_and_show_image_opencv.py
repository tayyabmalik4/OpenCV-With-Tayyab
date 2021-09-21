# (03)*****************Read and show image in opencv in python****************

# ----discuss about
# --Create file
# --How to show image?
# --Resize image
# --Slide show
# --4 images in one window
# --Multiple images in one window

# ----importing libraries
import cv2
import os
import numpy as np

# ----add path and pic
path = r"""D:\\machine learning practice\\openCV\\images"""
img_name= "IMG_4716.JPG"


# ---for reading the image path
# img = cv2.imread(path + "\\" + img_name)

# ----if we want to resize the image than we use resize function
# resize = cv2.resize(img,(600,400))

# ---for showing the image
# cv2.imshow('Image',resize)

# ----if we write 1 in the function of waitKey then pic destroy after 1 sec 
# ----But if we write 0 in the function of waitKey then pic destroy after press anykey of keyboard
# cv2.waitKey(0)


# cv2.destroyAllWindows()

# ----if we want to show multiple images at a one time than we use this method
images= os.listdir('D:\\machine learning practice\\openCV\\images')
# print(images)
# for i in images:
#     full_path = path + '\\' +i
#     img = cv2.imread(full_path)
#     resize = cv2.resize(img,(600,400))
#     cv2.imshow("Tayyab's Images" ,resize)
#     cv2.waitKey(1)
# cv2.destroyAllWindows()


# ----if we want to show one images into multiple times than we use this method
for i in images:
    full_path = path + "\\" + i
    img=cv2.imread(full_path)
    resize = cv2.resize(img,(600,400))
    img_2 = np.hstack((resize,resize))
    img_4 = np.vstack((img_2,img_2))
    cv2.imshow("Tayyab's Multiple photoes", img_4)
    cv2.waitKey(0)
cv2.destroyAllWindows()



