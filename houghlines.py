#import Libraries
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import math
##################################################

'''
This example illustrates how find lines in an image

Usage:
    houghlines.py [<image_name>]
    image argument defaults to board.jpg
'''


#Read from input
try:
	fn = sys.argv[1]
except IndexError:
        fn = "linefood.jpg"
##################################################


#Read image
img_original = mpimg.imread(fn,1)
img = mpimg.imread(fn,1)

#grascale it and find the edges with Canny algorithm
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
edges = cv2.Canny(gray,50,60,apertureSize = 3)
##################################################


#Find Lines with cv2.HoughLinesP function (probabilisticly)
minLineLength = 10
maxLineGap = 5
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 40, minLineLength, maxLineGap)
a,b,c = lines.shape
for i in range(a):
	cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 3, cv2.LINE_AA)


#Find Lines with cv2.HoughLinesP function (explicitly)
lines = cv2.HoughLines(edges, 1, math.pi/180.0, 100)
a,b,c = lines.shape
for i in range(a):
    rho = lines[i][0][0]
    theta = lines[i][0][1]
    a = math.cos(theta)
    b = math.sin(theta)
    x0, y0 = a*rho, b*rho
    pt1 = ( int(x0+1000*(-b)), int(y0+1000*(a)) )
    pt2 = ( int(x0-1000*(-b)), int(y0-1000*(a)) )
    cv2.line(img, pt1, pt2, (0, 0, 255), 3, cv2.LINE_AA)
##################################################


#test code
#cv2.imshow('houghlines3.jpg',edges)
#cv2.waitKey(0)
#cv2.imshow('houghlines3.jpg',img)
#cv2.waitKey(0)
##################################################


#organize the plots
plt.subplot(131), plt.imshow(img_original)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(edges,cmap = 'gray')
plt.title('Canny Edges Feature Extraction'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img)
plt.title('Hough Line Feature Extraction'), plt.xticks([]), plt.yticks([])
plt.show()
##################################################