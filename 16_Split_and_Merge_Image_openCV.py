# (16)*************Split and Merge Image in openCV using python************

# ----if we want o split image in single channal & Merge multiple single channel than we use this method

# ----importing libraries
import cv2

# ----define path of the image
path = r'images/5.JPG'
image = cv2.imread(path)
image = cv2.resize(image,(800,600)) # 3 channals
# image = cv2.resize(image[:,:,0],(800,600)) # for blue
# image = cv2.resize(image[:,:,1],(800,600))   # for Green
# image = cv2.resize(image[:,:,2],(800,600)) # for Red 

# ----when we split the image using numpy indexing
# ----in the image total channal 3 ---1st is blue ---2nd is Green--- 3rd is Red
# ----in the image shape total 3 parameters---1st is rows----2nd is columns ---3rd is channals
# image[:,:,0] # for blue
# image[:,:,1]   # for Green
# image[:,:,2] # for Red

# ----when we want to split the channals than we use split function in the openCV
b, g, r = cv2.split(image)
# print(b)
# print(b.shape)
# print(g)
# print(g.shape)
# print(r)
# print(r.shape)

# ---(Note---numpy array is more and more faster than cv2. so we mostly prefer numpy array to split the image indexing)

# ***********For Merging the image channals using rhe cv2.merge function
img_merge = cv2.merge([b,g,r])


# cv2.imshow("Car",image)
cv2.imshow("Car",img_merge)
cv2.waitKey(0)
cv2.destroyAllWindows() 