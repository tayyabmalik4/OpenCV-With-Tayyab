# (05)************Read Images in openCV in python************

# ----Definition---In order to load an image off of disk and display it using OpenCV, you first need to call the cv2. imread function, passing in the path to your image as the sole argument. Then, a call to cv2. imshow will display your image on your screen.

# ----imread function has taken 2 arguments path and flag
# --path means that the image or vedio path and flag means that the color of the image(default RGB)


# --importing libraries
import cv2

path = r'images/9.JPG'
# img = cv2.imread(path)

# ----if we want to show the image in RGB we use cv2.IMREAD_COLOR or 1
img = cv2.imread(path,cv2.IMREAD_COLOR)
# img = cv2.imread(path,1)

# ----if we want to show the image in black&white than we use cv2.IMREAD_GRAYSCALE or  0
# img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
# img = cv2.imread(path,0)

# ----if we want that the image color has not changed than we use cv2.IMREAD_UNCHANGED or -1
# img = cv2.imread(path,cv2.IMREAD_UNCHANGED)
# img = cv2.imread(path,-1)

# print(img)
# print(img.shape)
img= cv2.resize(img,(600,400))
cv2.imshow('tayyab',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
