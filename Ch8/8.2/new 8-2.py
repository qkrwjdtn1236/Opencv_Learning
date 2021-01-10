import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

while True:
    ret,img_color = capture.read()
    img_result = img_color.copy()

    height,width = img_color.shape[:2]

    center_x = int(width*0.5)
    center_y = int(height*0.5)

    #ROI 영역을 빨간색으로 표현
    cv.rectangle(img_result,(center_x-100,center_y-100),(center_x+100,center_y+100),(0,0,255),3)

    img_roi = img_color[center_y-100:center_y+100,center_x-100:center_x+100]
    #ROI의 영역 색 숫자에 대한 평균
    m = cv.mean(img_roi)

    img_mean = np.zeros(img_roi.shape,dtype=np.uint8)

    img_mean[:] = (m[0],m[1],m[2])
    cv.imshow('mean',img_mean)
    cv.imshow('colpor',img_result)
    cv.imshow('roi',img_roi)

    key = cv.waitKey(1)
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()