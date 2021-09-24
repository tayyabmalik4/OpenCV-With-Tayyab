# (14)****************Draw ploygons and Hexagon on image in openCV using python******************

# ----if we want to draw polygons or hexagon on image than we use polylines function in cv2

# ---importing libraries
import cv2
import numpy as np

# ----this is the path of image
img_path = r'images/3.JPG'

# ---for reading the image
image = cv2.imread(img_path)
img_resize = cv2.resize(image,(800,600))

# ---Appling the polylines function
# pts = np.array([[50,70],[70,90],[50,110],[40,130],[500,150]])
isClosed = True
color = (34,234,8)
thickness = 3
lineType = cv2.LINE_8
shift =0

# ----creat polyline function
# img_polygon = cv2.polylines(img_resize,[pts],isClosed,color,thickness,lineType,shift)

# ----if we want to creat hexagon shape than we use always polylines function just change the pts values
pts = np.array([[25,70],[25,145],
                [75,190],[150,190],
                [200,150],[200,70],
                [150,25],[75,25]],
                np.int32)
img_polygon = cv2.polylines(img_resize,[pts],isClosed,color,thickness,lineType,shift)

# ----if we want to draw rectangle, triangle or line by using polyline we use polylines function
rectangle = np.array([[10,5],[10,255],[50,225],[50,5]],np.int32)
triangle = np.array([[100,110],[150,190],[400,305],],np.int32)
line = np.array([[500,225],[700,225]],np.int32)

# ---this is for rectangle
# img_polygon = cv2.polylines(img_resize,[rectangle],isClosed,color,thickness,lineType,shift)

# ---this is for triangle
# img_polygon = cv2.polylines(img_resize,[triangle],isClosed,color,thickness,lineType,shift)

# ----this is for line
# img_polygon = cv2.polylines(img_resize,[line],isClosed,color,thickness,lineType,shift)

# ----if we want to put text in the line than we use putText function
# text = cv2.putText(img_polygon,"Amazing",(450,225),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,36,232),2)
text = cv2.putText(img_polygon,"OctaGon",(50,105),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,2,(255,36,232),2)



# ---for showing the image
# cv2.imshow("image",img_polygon)
cv2.imshow("image",text)
cv2.waitKey(0)
cv2.destroyAllWindows()