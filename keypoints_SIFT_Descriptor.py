#import Libraries
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
##################################################

'''
This example illustrates how to extract interesting key points
as features from an image

Usage:
    keypointsSIFTDescriptor.py [<image_name>]
    image argument defaults to fruits.jpg
'''

#Read from input
try:
	fn = sys.argv[1]
except IndexError:
        fn = "img/home.jpg"
##################################################

#Read image and plot it
img_original = mpimg.imread(fn)
img = mpimg.imread(fn)	
plt.subplot(121), plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

#grayscale it
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##################################################

#use SIFT descriptor for image key points feature extraction
sift = cv2.xfeatures2d.SIFT_create()
(kps, sift) = sift.detectAndCompute(gray, None)
##################################################

#draw the keypoints
img = cv2.drawKeypoints(gray,kps,None,None,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
plt.subplot(122), plt.imshow(img)
plt.title('Image with extracted keypoints'), plt.xticks([]), plt.yticks([])
plt.show()
##################################################