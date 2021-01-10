import cv2
img_gray = cv2.imread('cat on laptop.jpg',cv2.IMREAD_GRAYSCALE)

img_copyed1 = img_gray

print(id(img_gray),id(img_copyed1))

#cv2.line(img_gray,(0,0),(100,100),0,5)

ret,img_gray = cv2.threshold(img_gray,127,255,cv2.THRESH_BINARY)

print(id(img_gray),id(img_copyed1))

cv2.imshow('img_gray',img_gray)
cv2.imshow('img_copyed',img_copyed1)

cv2.waitKey(0)
cv2.destroyAllWindows()