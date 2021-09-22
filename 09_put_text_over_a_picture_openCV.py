# (09)*****************Put text over a picture in openCV using python**************

# ----importing libraries
import cv2
import numpy as np

# ----this is the path of imag
img_path = r"img_converter.png"

# ----for reading the image
image = cv2.imread(img_path)
image = cv2.resize(image,(600,400))

# ----this code is for puting text in the image
# ---putText function takes a many parameters like following
# ---cv2.putText(img, text, org, fontFace, fontScale, color, thickness=..., lineType=..., bottomLeftOrigin=...)

text = "Tayyab's picture"
org = (100,50)
font = cv2.FONT_HERSHEY_COMPLEX
fontScale = 0.5
color = (50,70,95) #---(B,G,R) and its value between 0 to 255
thickness = 0
linetype = cv2.LINE_AA
bottomLeftorigin = False

img_text = cv2.putText(image,text,org,font,fontScale,color,thickness,linetype,bottomLeftorigin)
# img_text = cv2.putText(image,text,org,font,fontScale,color,thickness,linetype,bottomLeftOrigin=True)

# ----for showing the image text in the image
cv2.imshow("Text Image", img_text)

cv2.waitKey(0)
cv2.destroyAllWindows()