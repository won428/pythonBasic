import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # 아래 경고 메시지 때문에 작성해줌

import matplotlib.pyplot as plt

from keras.src.legacy.preprocessing.image import ImageDataGenerator

idg = ImageDataGenerator(rescale=1/255, rotation_range=90, width_shift_range=1.0,
                       height_shift_range=0.5, shear_range=0.8, zoom_range=0.5,
                       horizontal_flip=True, vertical_flip=True)

print(f'type(idg): {type(idg)}')

image_source = './../img/' # 이미지를 가져 오는 위치
image_destination = './../dataOut/' # 이미지가 저장되는 위치
IMAGE_WIDTH, IMAGE_HEIGHT = 512, 512 # 다루고자 하는 이미지의 크기

# iters : 해당 디렉토리에서 읽어 들인 반복자(iterator) 객체입니다.
iters = idg.flow_from_directory(
            directory=image_source,
            target_size=(IMAGE_HEIGHT, IMAGE_WIDTH),
            classes=['cat', 'dog'], # 클래스 이름
            batch_size=4, # 한번에 읽어 들일 갯수
            color_mode='rgb', # 색상 채널 모드(grayscale, rgb, rgba)
            class_mode='binary', # 이항 분류
            shuffle=False )

# Found 20 images belonging to 2 classes.
# 2개의 클래스에 속해 있는 이미지 20개가 발견되었습니다.

print(f'type(iters): {type(iters)}') # DirectoryIterator 객체
print(f'한번에 실행할 사이즈 : {iters.batch_size}') # batch_size 속성과 연관 있음
print(f'이미지 형상 정보 : {iters.image_shape}') # target_size와 color_mode와 연관 있음
print(f'클래스 레이블과 색인 정보 : {iters.class_indices}')

print('next() 함수는 반복자(iterator) 객체인 iters에서 다음 항목을 읽어 주는 파이썬내장 함수입니다.')
x_train, y_train = next(iters)

print(f'len(x_train) : {len(x_train)}')
print(f'x_train.shape : {x_train.shape}') # (4, 512, 512, 3)

print(f'배치 사이즈 : {x_train.shape[0]}')
print(f'이미지 사이즈 : {x_train.shape[1:3]}')

color_mode = '컬러' if x_train.shape[3] == 3 else '흑백'
print(f'색상 모드 : {color_mode}')

print(f'y_train.shape : {y_train.shape}')

num_batches = len(iters) # 전체 배치 회수

cnt = 0 # 카운터 변수

for batch_idx in range(num_batches):
    x_batch, y_batch = iters[batch_idx] # 배치 사이즈 만큼 읽어 오기

    for idx in range(len(x_batch)):
        img = x_batch[idx]
        cnt += 1
        filename = f'generated_image_{str(cnt).zfill(2)}.png'
        plt.imshow(img)
        plt.axis('off')
        plt.savefig(image_destination + filename)
        print(f'{filename} 파일 저장 완료')
    # end inner for
# end outer for





