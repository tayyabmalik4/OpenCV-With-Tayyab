# *********************Change image color in openCV using python

# ----if we want to change the color of the image than we use cvtColor function in openCV library

# ----this is the website link of cv2.cvtColor---in this website gives all of the color codes
# ----https://docs.opencv.org/3.4.15/d8/d01/group__imgproc__color__conversions.html

# ---importing libraires
import cv2
import numpy as np

# ---define path
img_path = r'images/9.JPG'
image = cv2.imread(img_path)
resize = cv2.resize(image,(1000,800))

# -----if we want to change the color of the image we use cvtColor function in openCV
# cvt = cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
# cvt = cv2.cvtColor(resize,cv2.COLOR_BGR2HLS_FULL)
# cvt = cv2.cvtColor(resize,cv2.COLOR_BGR2Lab)

# ----we change the color as the name of color as well as number format
cvt = cv2.cvtColor(resize,3)


# cv2.imshow('image',resize)
cv2.imshow('image',cvt)
cv2.waitKey(0)
cv2.destroyAllWindows()
