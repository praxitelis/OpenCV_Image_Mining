#import Libraries
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
##################################################

'''
This example illustrates how find circles in an image

Usage:
    houghcircles.py [<image_name>]
    image argument defaults to board.jpg
'''


#Read from input
try:
	fn = sys.argv[1]
except IndexError:
        fn = "board.jpg"
##################################################


#Read image and plot it
img = cv2.imread(fn,0)
img_with_circles = cv2.imread(fn,1)
img_original = cv2.imread(fn,1)

#blur a bit the image in order to find more circles and grayscale it
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#organize the plots
plt.subplot(121), plt.imshow(img_original)
plt.title('Initial Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_with_circles)
plt.title('Circle Detection'), plt.xticks([]), plt.yticks([])
##################################################


#Find circles inside the image
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,40,
                            param1=100,param2=30,minRadius=1,maxRadius=30)
##################################################


#draw all the circles
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(img_with_circles,(i[0],i[1]),i[2],(255,0,0),2)
    # draw the center of the circle
    cv2.circle(img_with_circles,(i[0],i[1]),2,(255,0,255),3)
##################################################


#cv2.imshow('detected circles',img_with_circles)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
plt.show()