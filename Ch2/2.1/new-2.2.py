import cv2

#컬러 이미지로 파일을 읽어옵니다.
img_color = cv2.imread('cat on laptop.jpg',cv2.IMREAD_COLOR)

if img_color is None:
    print('이미지 파일을 읽을 수 없습니다.')
    exit(1)

#컬러 이미지를 먼저 화면에 보여주고
cv2.namedWindow('Color')
cv2.imshow('Color',img_color)

#대기하다가 키보드 입력이 있으면 다음 줄이 실행됩니다.
cv2.waitKey(0)

#img_color에 저장된 컬러 이미지를 그레이 스케일 이미지로 변환후
#img_gray에 대입합니다.
#COLOR_BGR2GRAY는 BGR 채널을 가진 컬러 이미지를 그레이 스케일로 변환하겠다고 지정해주는 겁니다.
img_gray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)

#img_gray에 저장된 그레이 스케일 이미지를 식별자가 'Grayscale'인 창이 보여줍니다.
#첫 번째 아규먼트를 앞에서 컬러 이미지 보여줄 때 사용한 'Color'창에 보이게 됩니다.

cv2.imshow('Grayscale',img_gray)
#img_gray에 저장된 이미지를 첫번째 아규먼트로 지정한 파일로 저장합니다.
#이미지 포맷은 지정한 파일의 확장자에 따라 결정됩니다.
cv2.imwrite('new_grayscale.jpg',img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()