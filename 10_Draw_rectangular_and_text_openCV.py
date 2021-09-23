# (10)**********************How do you draw a rectangular and text in openCV using python*************

# ----when we generate a vedio or object detection than we use rectangular function in it

# ----importing libraries
import cv2
import numpy as np

img_path = r"img_converter.png"

# ----for reading the image path
image = cv2.imread(img_path)

# ----for resizing the image
image = cv2.resize(image,(1000,800))

# ----these are the parameters of rectangular function in opencv
# ----cv2.rectangle: (img, pt1, pt2, color, thickness=..., lineType=..., shift=...)
# ----pt1 means that the axis x1 and y1
# ----pt2 means that the axis x2 and y2
# ----color mean the color of the ractangle
# ----thickness means the thickness of the lines
# ----linetype is a optional but its means what type of line which we use
# ----shift is also optional
pt1=(200,50)  
pt2 = (400,300)
color = (0,255,0) #(B,G,R) the number is between 0 to 255
# ----if we want to fill the rectangle than we use -1 value in the place of thickness values for example
# thickness = -1
thickness = 3
lineType = cv2.LINE_4

img_ract = cv2.rectangle(image,pt1,pt2,color,thickness,lineType)
img_ract1 = cv2.rectangle(image,(500,70),(700,200),color,thickness,lineType)

# ----if we want to putText in the upper side of ractangle than we use putText function
# ----text on image
text = "Face - 100%"
org = (200,40)
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontScale = 0.8
color =(255,0,0) #(B,G,R)
lineType = cv2.LINE_4
thicknesss = 1

img_text = cv2.putText(img_ract,text,org,fontFace,fontScale,color,thicknesss,lineType)

# ----if we want to save the image than we use imwrite function
cv2.imwrite("tut_10_object Detection.png",img_text)

# ----for showing the image
cv2.imshow("Rectangle on Image",img_text)

# ----for waiting the showing image
cv2.waitKey(0)
cv2.destroyAllWindows()
