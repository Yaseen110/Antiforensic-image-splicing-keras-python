import cv2
import numpy as np
from skimage.metrics import structural_similarity
# Reading the image
image = cv2.imread('bg5.jpg')
cv2.imshow('Original', image)
kernel1 = (1/16)*np.array([[1,2,1],[2,4,2],[1,2,1]])
img1 = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)
cv2.imshow('Kernel Blur', img1)
kernel2 = (1/100)*np.array([[1,2,4,2,1],[2,4,8,4,2],[4,8,16,8,4],[2,4,8,4,2],[1,2,4,2,1]])
img2 = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
cv2.imshow('Kernel Blur2', img2)
(score1, diff1) = structural_similarity(image, img1, full=True,channel_axis=2)
print("Image similarity", score1)
(score2, diff2) = structural_similarity(image, img2, full=True,channel_axis=2)
print("Image similarity", score2)
cv2.waitKey()