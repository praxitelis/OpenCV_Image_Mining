#import Libraries
import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
##################################################

'''
This example illustrates how find the color histogram in an image.

Usage:
    hist.py [<image_name>]
    image argument defaults to fruits.jpg
'''


#Read from input
try:
	fn = sys.argv[1]
except IndexError:
        fn = "img/fruits.jpg"
##################################################


#Read image and plot it
img = mpimg.imread(fn)	
plt.subplot(121), plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
##################################################


#Get the histogram
hist = cv2.calcHist([img],[0],None,[256],[0,256])
##################################################


#Plot the histogram in 3 rgb channels and plot it by each channel
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.subplot(122), plt.plot(histr,color = col)
    plt.title('Image Histogram'),plt.xlim([0,256])
plt.show()
##################################################