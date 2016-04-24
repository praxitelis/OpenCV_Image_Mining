#import Libraries
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
##################################################

'''
This example illustrates how to descrease the brightness in an image.

Usage:
    houghcircles.py [<image_name>, <brightness_value_to_descrease>]
    image argument defaults to winlogo.jpg
'''

#Read from input
try:
	fn = sys.argv[1]
	light = sys.argv[2]
except IndexError:
        fn = "winLogo.jpg"
	light = 64
##################################################
 
#Read image and plot it
im = mpimg.imread(fn)
plt.subplot(121), plt.imshow(im)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
##################################################


#get with threshold the image with lower brightness
ret,thresh = cv2.threshold(im,light,255,cv2.THRESH_TRUNC)
##################################################


#plot the darker image
plt.subplot(122), plt.imshow(thresh)
plt.title('With less brightness, threshold: %s' %light), plt.xticks([]), plt.yticks([])
plt.show()
##################################################