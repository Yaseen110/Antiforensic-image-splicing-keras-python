import os
import cv2 as cv
import numpy as np
import pandas as pd
from skimage.metrics import structural_similarity
# from pykuwahara import kuwahara
def fil(i,img):
    mean = 10
    stddev = 30
    noise = np.zeros(img.shape, np.uint8)
    cv.randn(noise, mean, stddev)
    img1 = cv.add(img, noise)
    return img1
# print(os.listdir('dataset/test'))
scores=[]
for i in os.listdir('dataset/test'):
    for j in os.listdir('dataset/test/'+i):
        img=cv.imread('dataset/test/'+i+'/'+j)
        img2=fil(i,img)
        (score1, diff1) = structural_similarity(img, img2, full=True,channel_axis=2)
        scores.append(score1)
        # cv.imwrite('filters/noise_filter/noise/'+i+'/'+j,img2)
        # cv.imshow(i,img)
dict1={"SSIM":scores}
final=pd.DataFrame(dict1)
final.to_csv("filters/N2.csv")
cv.waitKey(0)