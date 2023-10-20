import os
import cv2 as cv
import numpy as np
import pandas as pd
from skimage.metrics import structural_similarity
from pykuwahara import kuwahara
def fil(i,img):
    blur1=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
    return blur1
# print(os.listdir('dataset/test'))
scores=[]
for i in os.listdir('dataset/test'):
    for j in os.listdir('dataset/test/'+i):
        img=cv.imread('dataset/test/'+i+'/'+j)
        img2=fil(i,img)
        (score1, diff1) = structural_similarity(img, img2, full=True,channel_axis=2)
        scores.append(score1)
        cv.imwrite("filters/test_filter/gaussian_blur/5_X_5/"+i+'/'+j,img2)
        # cv.imshow(i,img)
dict1={"GB5":scores}
final=pd.DataFrame(dict1)
final.to_csv("filters/GB5.csv")
cv.waitKey(0)