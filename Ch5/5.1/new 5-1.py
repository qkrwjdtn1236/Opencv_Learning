import cv2 as cv

img_color = cv.imread('grayscale.png',cv.IMREAD_COLOR)

if img_color is None:
    print('이미지를 불러올 수 없습니다.')
    exit(1)

img_gray = cv.cvtColor(img_color,cv.COLOR_BGR2GRAY)

ret, img_binary = cv.threshold(img_gray,127,255,cv.THRESH_BINARY)

cv.imshow('Grayscale',img_gray)
cv.imshow('Binary',img_binary)

cv.waitKey(0)
cv.destroyAllWindows()