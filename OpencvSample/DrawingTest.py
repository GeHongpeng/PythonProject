# _*_ coding: utf-8 _*_

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image(color)
img = np.zeros((512,512,3), np.uint8)
# Create a black image(nocolor)
#img = np.zeros((512,512), np.uint8)

# Draw a diagonal blue line
# (0,0) start point
# (511,511) end point
# (255,0,0) BGR color
cv2.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a rectangle
"""
Rectangle(img, pt1, pt2, color, thickness=1, lineType=8, shift=0)
img – Image.
pt1 – Vertex of the rectangle.
pt2 – Vertex of the rectangle opposite to pt1 .
rec – Alternative specification of the drawn rectangle.
color – Rectangle color or brightness (grayscale image).
thickness – Thickness of lines that make up the rectangle. Negative values, like CV_FILLED , mean that the function has to draw a filled rectangle.
lineType – Type of the line. See the line() description.
shift – Number of fractional bits in the point coordinates.
"""
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Dram a circle
"""
Circle(img, center, radius, color, thickness=1, lineType=8, shift=0)
img – Image where the circle is drawn.
center – Center of the circle.
radius – Radius of the circle.
color – Circle color.
thickness – Thickness of the circle outline, if positive. Negative thickness means that a filled circle is to be drawn.
lineType – Type of the circle boundary. See the line() description.
shift – Number of fractional bits in the coordinates of the center and in the radius value.
"""
cv2.circle(img,(447,63),63,(0,0,255),-1)

# Draw a ellipse
"""
Ellipse(img, center, axes, angle, start_angle, end_angle, color, thickness=1, lineType=8, shift=0)
angle – Ellipse rotation angle in degrees.
startAngle – Starting angle of the elliptic arc in degrees.
endAngle – Ending angle of the elliptic arc in degrees.
color – Ellipse color.
thickness – Thickness of the ellipse arc outline, if positive. Otherwise, this indicates that a filled ellipse sector is to be drawn.
lineType – Type of the ellipse boundary. See the line() description.
shift – Number of fractional bits in the coordinates of the center and values of axes.
"""
cv2.ellipse(img,(256,256),(100,50),0,0,180,(255,0,0),-1)

# Draw a polylines
"""
PolyLine(img, polys, is_closed, color, thickness=1, lineType=8, shift=0)
img – Image.
pts – Array of polygonal curves.
npts – Array of polygon vertex counters.
isClosed – Flag indicating whether the drawn polylines are closed or not. If they are closed, the function draws a line from the last vertex of each curve to its first vertex.
color – Polyline color.
thickness – Thickness of the polyline edges.
lineType – Type of the line segments. See the line() description.
shift – Number of fractional bits in the vertex coordinates.
"""
pts=np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))

# Add Text to Image
"""
PutText(img, text, org, fontFace, fontScale, color, thinkness)
img – Image.
text – Text string to be drawn.
org – Bottom-left corner of the text string in the image.
font – CvFont structure initialized using InitFont().
fontFace – Font type. One of FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN, FONT_HERSHEY_DUPLEX, FONT_HERSHEY_COMPLEX, FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL, FONT_HERSHEY_SCRIPT_SIMPLEX, or FONT_HERSHEY_SCRIPT_COMPLEX, where each of the font ID’s can be combined with FONT_ITALIC to get the slanted letters.
fontScale – Font scale factor that is multiplied by the font-specific base size.
color – Text color.
thickness – Thickness of the lines used to draw a text.
lineType – Line type. See the line for details.
bottomLeftOrigin – When true, the image data origin is at the bottom-left corner. Otherwise, it is at the top-left corner.
"""
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
