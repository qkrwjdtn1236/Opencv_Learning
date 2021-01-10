import cv2 as cv
import numpy as np

img_color = cv.imread('cat.jpg')
cv.imshow('original',img_color)

height,width = img_color.shape[:2]
M = np.float32([[1,0,100],[0,1,50]]) # 오른쪽으로 100만큼, 아래로 50만큼 이동시킬려는 배열

img_translation = cv.warpAffine(img_color,M,(width,height))

cv.imshow('translation',img_translation)

cv.waitKey(0)
cv.destroyAllWindows()