import cv2 as cv
from skimage.metrics import structural_similarity
from pykuwahara import kuwahara
img=cv.imread("bg5.jpg")
cv.imshow('header',img)
filt1 = kuwahara(img, method='mean', radius=3)
filt2 = kuwahara(img, method='gaussian', radius=3) 
cv.imshow('filt1',filt1)
cv.imshow('filt2',filt2)
(score1, diff1) = structural_similarity(img, filt1, full=True,channel_axis=2)
(score2, diff2) = structural_similarity(img, filt2, full=True,channel_axis=2)
print("Image similarity", score1)
print("Image similarity", score2)
cv.waitKey(0)