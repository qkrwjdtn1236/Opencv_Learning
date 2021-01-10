import cv2 as cv
import numpy as np

img_gray = cv.imread('test.png',cv.IMREAD_GRAYSCALE)

kernal = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
img_result = cv.erode(img_gray,kernal,iterations=1)

cv.imshow('Input',img_gray)
cv.imshow('Result',img_result)

cv.waitKey(0)
cv.destroyAllWindows()