import cv2 as cv

def nothing(x):
    pass


cv.namedWindow('Binary')
cv.createTrackbar('threshold','Binary',0,255,nothing)
cv.setTrackbarPos('threshold','Binary',127)

img_color = cv.imread('ball.jpg',cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color,cv.COLOR_BGR2GRAY)

while True:
    thre = cv.getTrackbarPos('threshold','Binary')

    ret, img_binary = cv.threshold(img_gray,thre,255,cv.THRESH_BINARY_INV)
    img_result = cv.bitwise_and(img_color,img_color,mask=img_binary)

    cv.imshow('Result',img_result)
    cv.imshow('Binary',img_binary)

    if cv.waitKey(1) == 27:
        break

cv.destroyAllWindows()