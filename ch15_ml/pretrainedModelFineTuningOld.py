import os

from keras.src.legacy.preprocessing.image import ImageDataGenerator

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # 아래 경고 메시지 때문에 작성해줌
# 2025-12-11 18:01:07.916279: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
# 2025-12-11 18:01:10.574809: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
# To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.

import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
from keras.src.utils import load_img, img_to_array
from keras.src.applications.vgg16 import VGG16, preprocess_input, decode_predictions

IMAGE_WIDTH, IMAGE_HEIGHT = 224, 224 # VGG16 모델의 이미지 정보
image_source = './../dataIn/image/' # 이미지를 읽어 들일 경로
image_destination = './../dataOut/' # 이미지 파일이 저장될 경로

# weights : ImageNet 데이터 셋에서 학습했던 모델 정보를 그대로 사용하겠습니다.
# include_top=False : 1000개의 클래스를 무시하고, 내가 10개로 하겟습니다.
# input_shape : 입력 이미지 크기를 지정하는 부분
model = VGG16(weights='imagenet', include_top=False, input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3))

model.trainable = False # 사전 학습 모델 정보는 다시 내가 학습시키지 않겠습니다.
# 다만 우리가 다시 추가하는 Dense 층들만 학습시킬께요.

from keras import Model

from keras.src.layers import Dense, MaxPooling2D, Dropout

# Custom Classifier 생성
x = model.output
x = MaxPooling2D()(x) # 일종의 가지 치기

# activation : 활성화 함수
# 마지막 레이어가 아닌 레이에서는 주로 'relu' 활성화 함수를 많이 사용합니다.
x = Dense(units=256, activation='relu')(x)

x = Dropout(0.5)(x) # 노드의 일부를 off
x = Dense(units=128, activation='relu')(x)

# 마지막 레이어의 노드 개수(units)는 클래스 갯수와 동일해야 합니다.
# 'softmax'는 다항 분류에 사용되는 활성화 함수입니다.
outputs = Dense(units=10, activation='softmax')(x)

model = Model(inputs=model.input, outputs=outputs)

print(model.summary())
# 입력 : (None, 224, 224, 3) : 크기 224*224 컬러 이미지
# 출력 : (None, 10) 개발자가 정의한 클래스 갯수가 보입니다.

# loss : 손실 함수, optimizer : 최적화 알고리즘, metrics : 평가 지표
# 이항 분류 손실 함수 : 'binary_crossentropy'
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

file_list = os.listdir(image_source)

total_data = [] # 예측을 하기 위한 vgg16 모델에 맞게 전처리된 이미지 모음

for filename in file_list:
    myfile = image_source + filename
    # 모델이 요구하는 이미지 사이즈로 변경
    current_image = load_img(myfile, target_size=(IMAGE_WIDTH, IMAGE_HEIGHT))
    plt.imshow(current_image)
    plt.axis('off')

    saved_file = image_destination + 'pretrained_model_' + filename
    plt.savefig(saved_file)
    print(f'{filename} 파일이 저장되었습니다.')

    ndarray = img_to_array(current_image)
    # print(ndarray) # n(정수) d(dimension) array(배열)

    # 가로 세로 각각 224픽셀이고, 컬러 이미지입니다.
    print(f'형상 : {ndarray.shape}') # 형상 : (224, 224, 3)

    print('사전 학습 모델의 환경과 동일하게 맞춰 줍니다.')
    pre_input = preprocess_input(ndarray)
    # print(pre_input)
    print(f'pre_input 형상 : {pre_input.shape}')  # 형상 : (224, 224, 3)

    total_data.append(pre_input)
# end for

import numpy as np

# x_train : 사전 학습 모델을 사용하기 때문에, x_train는 필요 없습니다.
# x_test : 사전 학습 모델에 테스트하고자 하는 입력 데이터 입니다.
x_train = np.stack(total_data)

# Data Augmentation
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True
)

# Fine-tuning 레이어 지정
for layer in model.layers[-4:]:
    layer.trainable = True
# end for (trainable layer loop)

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

prediction = model.predict(x_train)
print(prediction.shape) #  = (배치수, 3)


# image_gaesu = x_test.shape[0]
# color_name = '컬러' if x_test.shape[3] == 3 else '흑백'
# print(f'\n{color_name} 이미지가 {image_gaesu}개입니다.')
# print(f'픽셀 가로 : {x_test.shape[1]}, 픽셀 세로 : {x_test.shape[2]}')
#
# prediction = model.predict(x_test)
# image_size = prediction.shape[0]
# class_size = prediction.shape[1]
#
# print(f'\n입력 이미지의 갯수는 {image_size}개이고, ', end='')
# print(f'클래스의 갯수는 {class_size}입니다.')
# print('prediction에는 확률 값이 들어 있습니다.')
#
print('\n예측값 표시')
topN = 5 # 10개의 클래스 중에서 확률이 높은 상위 몇개
probability = []
print(probability)

for pred_idx, pred in enumerate(prediction):
    # top_idx = pred.argsort()[::-1][:topN]
    N = min(topN, pred.size)
    top_idx = pred.argsort()[::-1][:N]
    top_prob = pred[top_idx]

    top_prob = pred[top_idx]

    prob_list = [(int(idx), f"class_{idx}", float(prob))
                 for idx, prob in zip(top_idx, top_prob)]
    probability.append(prob_list)

    print(f'\n{pred_idx}번 이미지 TOP-{topN} 예측')
    for idx, prob in zip(top_idx, top_prob):
        print(f'클래스 {idx}, 확률 {prob:.4f}')
    # end inner for (print top predictions)
# end for (prediction loop)

# CSV 저장
csv_list = []
for idx in range(len(file_list)):
    for prob in probability[idx]:
        csv_list.append([file_list[idx], prob[1], prob[2]])
    # end inner for
# end outer for

df = pd.DataFrame(csv_list, columns=['image', 'description', 'probability'])
df.to_csv(image_destination + 'prediction_result.csv', index=False)
print('prediction_result.csv 파일이 저장되었습니다.')

# 시각화
mycolor = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '#FF1493', '#FF00CC', '#FFA500']

for idx, prob_list in enumerate(probability):
    plt.figure(figsize=(10, 8))
    captions = [item[1] for item in prob_list]
    data = [100.0 * item[2] for item in prob_list]

    Series(data, index=captions).plot(kind='bar', rot=12, color=mycolor[:len(captions)])
    plt.title(f'이미지 {file_list[idx]} 분류 결과', size=15)
    plt.ylim([-10, 100])
    plt.grid(True)

    filename = f'{image_destination}probability_{file_list[idx]}'
    plt.savefig(filename)
    print(f'{filename} 파일이 저장되었습니다.')
# end for (visualization loop)

print('Fine-Tuning 완료!')