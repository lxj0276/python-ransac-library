from __future__ import division
import cv2
from matplotlib import pyplot as plt
import numpy as n
from pyransac.ransac import RansacFeature
from pyransac.features import Circle

# Extract a frame from the provided video
video = cv2.VideoCapture('media/HRE-video.avi')
video.set(cv2.CAP_PROP_POS_FRAMES,70)
succ, frame = video.read()

# Set Gray Color
frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

# Init RansacFeature class for circle detection
ransac_process = RansacFeature(Circle,max_it = 100, inliers_percent=0.7,dst=2,threshold=100)

# Process the frame to detect the circle
dc,percent = ransac_process.image_search(frame)

# Super impose the detected feature on the image

theta = n.linspace(-n.pi,n.pi,100)
plt.imshow(frame, cmap='gray')
x,y = dc.print_feature(100)

# Reverted x,y because 
# OpenCV uses numpy.ndarray
# to store images and
# image[:,0] is the vertical
# axis of it. 
# See: http://stackoverflow.com/q/30681997/1334711

plt.plot(y,x,'r-',linewidth=2)
plt.axis('off')
plt.show()