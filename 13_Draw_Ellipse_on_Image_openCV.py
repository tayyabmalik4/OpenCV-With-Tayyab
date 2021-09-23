# (13)****************Draw Ellipse on image in openCV using Python**************

# -----Sometimes we use ellips in the algorithm so we learnt it

# ----importing libraries
import cv2

img_path = r'images/4.jpg'

img = cv2.imread(img_path)
img_resize = cv2.resize(img,(800,600))

# ---these are the parameters of ellips---ellipse: (img, center, axes, angle, startAngle, endAngle, color, thickness=..., lineType=..., shift=...)
# ---creating ellips
center = (500,250)
axes = (100,200)
angle = 30
startangle = 0
endangle = 360
color = (230,248,132)
thickness = 3
# +----if we want to fill the ellips than we use nagitive value in the thickness parameter
# thickness = -1
lineType = cv2.LINE_8
shift = 0

img_ellips = cv2.ellipse(img_resize,center,axes,angle,startangle,endangle,color,thickness,lineType,shift)
# ----creating 2nd ellips
img_ellips = cv2.ellipse(img_resize,(230,200),(100,50),10,0,360,(233,12,45),2,cv2.LINE_8,shift)

# ----if we want to put text in the ellips than we use putText function
text = cv2.putText(img_ellips,'Ellips',(450,250),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,2,(23,223,255),2,cv2.LINE_8)

cv2.imshow("image",text)
# cv2.imshow("image",img_ellips)
# cv2.imshow("image",img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()