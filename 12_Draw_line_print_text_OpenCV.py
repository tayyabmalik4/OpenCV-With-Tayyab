# (12)*****************Draw line and also print text on image in openCV using python***************

# ----sometimes we draw a line on the image when we use this method

# ----importing libraries
import cv2
import numpy as np

# ----importing path on image
img_path = r'images/5.jpg'
# ----for reading the image
img = cv2.imread(img_path)
img_resize = cv2.resize(img,(800,600))

# ----Now we draw a line on the image
# ----these are the parameters of the line function
# ---- line: (img, pt1, pt2, color, thickness=..., lineType=..., shift=...)
pt1 = (400,40)
pt2 = (600,40)
color =(255,0,0)
thickness = 10
lineType = cv2.LINE_8
shift = 0

# ----for creating the line on image
line = cv2.line(img_resize,pt1,pt2,color,thickness,lineType,shift)
line2 = cv2.line(img_resize,(100,40),(300,40),(0,233,43),thickness,lineType,shift)

# ----if we want to put the text on the line than we use putText function in the image
img_text = cv2.putText(line,"This is Line",(400,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,24,255),1,cv2.LINE_AA)
img_text = cv2.putText(line2,"Respected Sir",(100,30),cv2.FONT_HERSHEY_COMPLEX,0.5,(111,244,25),1,cv2.LINE_AA)


# ----for showing the image
cv2.imshow("Tayyab's picture",line)
cv2.waitKey()
cv2.destroyAllWindows()
