import cv2 as cv
import numpy as np
img=cv.imread("filters/experiments/bg5.jpg")
cv.imshow("header",img)
mean = 0
stddev = 10
noise = np.zeros(img.shape, np.uint8)
cv.randn(noise, mean, stddev)
noisy_img1 = cv.add(img, noise)
cv.imshow("noisy image1",noisy_img1)
cv.imwrite("noisy.jpg",noisy_img1)
cv.waitKey(0)