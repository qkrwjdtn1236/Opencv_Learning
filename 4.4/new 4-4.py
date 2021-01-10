import cv2 as cv


img_gray = cv.imread('ball.png',cv.IMREAD_GRAYSCALE)

img_canny = cv.Canny(img_gray,90,180)

cv.imshow('gray',img_gray)
cv.imshow('canny',img_canny)

cv.waitKey(0)
cv.destroyAllWindows()