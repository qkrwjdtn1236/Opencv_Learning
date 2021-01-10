import cv2 as cv

def on_trackbar(x):
    pass

img_color = cv.imread('red ball.png',cv.IMREAD_COLOR)

if img_color is None:
    print('이미지 파일을 읽을 수 없습니다.')
    exit(1)

img_gray = cv.cvtColor(img_color,cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',img_gray)

cv.namedWindow('Binary')
cv.createTrackbar('threshold','Binary',0,255,on_trackbar)
cv.setTrackbarPos('threshold','Binary',127)

while 1:
    thresh = cv.getTrackbarPos('threshold','Binary')
    #82값이 원활하다
    ret,img_binary = cv.threshold(img_gray,thresh,255,cv.THRESH_BINARY_INV)

    cv.imshow('Binary',img_binary)

    key = cv.waitKey(1)

    if key == 27:
        break


cv.destroyAllWindows()