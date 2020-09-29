import cv2 as cv

#카메라에서 이미지를 캡처하기 위해서는 VideoCapture 객체를 생성하여 카메라와 연경해야합니다.
#카메라 인덱스를 아규먼트로 사용합니다.
#PC에 처음 연결한 카메라의 인덱스는 0
#2번째로 연결한 카메라의 인덱스는 1
#이런 식으로 PC에 카메라를 연결한 순서에 맞추어 카메라에 접근할 때 사용하는 인덱스가 부여됩니다.

#카메라가 없을경우 실행이 불가능함.
#윈도우 카메라 캡처중지하고나서 에러가 발생되었을 경우, cv.CAP_DSHOW 입력하면 해결될겁니다.
cap = cv.VideoCapture(0,cv.CAP_DSHOW)

#카메라와 성공저그로 연결되었는지 체크합니다.
if cap.isOpened() == False:
    print('카메라를 열 수 없습니다.')
    exit(1)

#카메라에서 이미지 캡처와 윈도우에 이미지 보여주는 것을 반복하면 동영상처럼 보이게 됩니다.
while 1:
    #카메라에서 이미지를 읽어옵니다.
    ret, img_frame = cap.read()

    #ret 리턴값이 False 이면 캡처가 실패한 것입니다.
    if ret == False:
        print('캡처 실패')
        break

    #캡처된 이미지를 윈도우에 보여줍니다.
    cv.imshow('Color',img_frame)

    #사용자의 키보드 입력을 1밀리세컨드 동안 기다렸다가 다음줄을 실행합니다.
    key = cv.waitKey(1)

    #ESC 키가 입력되었다면 반복을 중지합니다.
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()