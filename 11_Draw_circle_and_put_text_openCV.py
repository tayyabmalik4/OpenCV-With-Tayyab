# (11)********************Draw circle and put text in openCV using python**************

# ----when we detect object than we mostly use circle or ractangle.

# ---importing libraries
import cv2
import numpy as np

img_path = r'images/1.JPG'
image = cv2.imread(img_path)
img_resize = cv2.resize(image,(1000,600))

# ----creating a circle
# ----these are the parameters of circle----(img, center, radius, color, thickness=..., lineType=..., shift=...)
center =(500,150)
radius =150
color = (0,0,255) #(B,G,R)
thickness = 3
# ----if we want to fill the circle than we use negative value
# thickness = -1
lineType = cv2.LINE_8
shift = 0

# ----creating circle
img_circle = cv2.circle(img_resize,center,radius,color,thickness,lineType,shift)
# ----creating 2nd circle
img_circle2 = cv2.circle(img_resize,(200,300),70,(200,255,0),thickness,lineType,shift)

# ----if we want to  put text in the circle than we use putText function
img_text = cv2.putText(img_circle,'wow',(450,100),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),1,lineType=cv2.LINE_4)

# ----Adding 2nd text
img_text = cv2.putText(img_circle2,'Great',(150,300),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1,lineType=cv2.LINE_4)


# ----showing the image
cv2.imshow("Tayyab's Image",img_text)
cv2.waitKey()
cv2.destroyAllWindows()