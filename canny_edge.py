#import Libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import matplotlib.image as mpimg
##################################################

'''
This example illustrates how edges in an image

Usage:
    canny_edge.py [<image_name>]
    image argument defaults to fruits.jpg
'''


#Read from input
try:
	fn = sys.argv[1]
except IndexError:
        fn = "fruits.jpg"
##################################################


#Read image and and find the edges inside
img = mpimg.imread(fn)
edges = cv2.Canny(img,100,200)
##################################################


#plot both image and the image with edges
plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image Feature'), plt.xticks([]), plt.yticks([])
plt.show()
##################################################
