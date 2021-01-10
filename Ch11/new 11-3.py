import cv2 as cv
import numpy as np

img_gray = cv.imread('test2.png',cv.IMREAD_GRAYSCALE)
kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))

img_result = cv.morphologyEx(img_gray,cv.MORPH_OPEN,kernel)

cv.imshow('Input',img_gray)
cv.imshow('result',img_result)

cv.waitKey(0)
cv.destroyAllWindows()