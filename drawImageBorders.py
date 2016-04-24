#import Libraries
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
##################################################

'''
This example illustrates how to draw image borders
and image's shapes borders

Usage:
    houghlines.py [<image_name>]
    image argument defaults to opencvLogo.png
'''


#Read from input
try:
	fn = sys.argv[1]
except IndexError:
        fn = "opencvLogo.png"
##################################################


#Read image
img = cv2.imread(fn)
image_original = cv2.imread(fn)

#grayscale it (for better accuracy)
imgray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

#and then seperate the interesting area with threshold function
ret,thresh = cv2.threshold(imgray,200,255,0)
##################################################

#find image boundary points
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#draw image boundary points
img_with_boundaries = cv2.drawContours(img, contours, -1, (127,127,0), 5)
##################################################


#organize the plots
plt.subplot(121), plt.imshow(image_original)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_with_boundaries)
plt.title('Image with drawn boundaries'), plt.xticks([]), plt.yticks([])
plt.show()
##################################################