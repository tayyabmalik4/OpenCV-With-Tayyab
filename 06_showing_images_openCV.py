# (06)**********************Showing the images in OpenCV using python**************

# ---Syntax--cv2.imshow(window name,ndarray)

# ----importing libraries
import cv2
import numpy as np

# ----showing the image in matrix
# matx = np.zeros((2000,2000))
# cv2.imshow('show image',matx)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ----showing the real image

path = r'images/IMG_4843.JPG'
img = cv2.imread(path)
img = cv2.resize(img,(600,400))
# ----if we want to show the same image but multiple windows than the window name is always unique
# ----if we want to show the same image but multiple windows than the window name is always unique
cv2.imshow('Model image',img)
cv2.imshow('Model image 1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
