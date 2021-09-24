# (17)*********Convert color or gray image to blue green and red image************

# ----sometime we need to convert RGB color image to gray color image and gray image to convert RGB or red green and blue images than we use this method

# ----importing library
import cv2
import numpy as np

# ----define path
path = r'images/10.png'
image = cv2.imread(path)
resize = cv2.resize(image,(800,600))

# ----split the channals into blue,green,red
b,g,r = cv2.split(resize)

# ----if we want to show image in just blue light than green and red light is totally off. so we creats the zeros values of image
zeros_ch = np.zeros(resize.shape[0:2],dtype='uint8')
blue_image = cv2.merge([b,zeros_ch,zeros_ch])

# ----for creating only green image color
green_image = cv2.merge([zeros_ch,g,zeros_ch])

# ----forcreating only red image color
red_image = cv2.merge([zeros_ch,zeros_ch,r])


# ----show image
# cv2.imshow('image',resize)
# cv2.imshow('image',b)
# cv2.imshow('image',g)
# cv2.imshow('image',r)
# cv2.imshow('Blue Image',blue_image)
# cv2.imshow('Blue Image',green_image)
# cv2.imshow('Blue Image',red_image)


# **************if we want to show the 4 images in one window than we use this method
path1 = r'images/12.png'
img = cv2.imread(path1)
img = cv2.resize(img,(400,400))

# ---for blue image
blue_array = np.zeros(img.shape,dtype='uint8')
blue_array[:,:,0] = img[:,:,0]

green_array = np.zeros(img.shape,dtype='uint8')
green_array[:,:,1] = img[:,:,1]

red_array = np.zeros(img.shape,dtype='uint8')
red_array[:,:,2] = img[:,:,2]

ht1 = np.hstack((red_array,green_array))
ht2 = np.hstack((blue_array,img))
img_4 = np.vstack((ht1,ht2))

cv2.imshow('4 images',img_4)
cv2.waitKey(0)
cv2.destroyAllWindows()