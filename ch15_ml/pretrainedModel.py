import os

from pandas import Series

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # 아래 경고 메시지 때문에 작성해줌
# 2025-12-11 18:01:07.916279: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
# 2025-12-11 18:01:10.574809: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
# To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.

import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False
from keras.src.utils import load_img, img_to_array
from keras.src.applications.vgg16 import VGG16, preprocess_input, decode_predictions

model = VGG16()
print(model.summary())
# 입력 : (None, 224, 224, 3) : 크기 224*224 컬러 이미지
# 출력 : (None, 1000) 최종 결과는 클래스 갯수가 1000개입니다.

IMAGE_WIDTH, IMAGE_HEIGHT = 224, 224 # VGG16 모델의 이미지 정보
image_source = './../dataIn/image/' # 이미지를 읽어 들일 경로
image_destination = './../dataOut/' # 이미지 파일이 저장될 경로

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
x_test = np.stack(total_data)

image_gaesu = x_test.shape[0]
color_name = '컬러' if x_test.shape[3] == 3 else '흑백'
print(f'\n{color_name} 이미지가 {image_gaesu}개입니다.')
print(f'픽셀 가로 : {x_test.shape[1]}, 픽셀 세로 : {x_test.shape[2]}')

prediction = model.predict(x_test)
image_size = prediction.shape[0]
class_size = prediction.shape[1]

print(f'\n입력 이미지의 갯수는 {image_size}개이고, ', end='')
print(f'클래스의 갯수는 {class_size}입니다.')
print('prediction에는 확률 값이 들어 있습니다.')

print('\n예측값 표시')
topN = 10 # 확률이 높은 상위 몇개
probability = decode_predictions(prediction, top=topN)
print(probability)

print('csv 파일을 작성합니다.')
csv_list = []

for idx in range(len(file_list)):
    print(f'이미지 `{file_list[idx]}`의 확률 값 정보를 수집합니다.')
    for prob in range(len(probability[idx])):
        # sublist(이미지이름, 클래스이름, 확률값)
        sublist = [
            file_list[idx],
            probability[idx][prob][1],
            probability[idx][prob][2]
        ]

        csv_list.append(sublist)
    # end inner for
# end outer for

print(csv_list)

import pandas as pd

model_columns = ['image', 'class name', 'probability']
model_frame = pd.DataFrame(csv_list, columns=model_columns)
filename = 'prediction_result.csv'
model_frame.to_csv(image_destination + filename, index=False)
print(f'{filename} 파일이 저장되었습니다.')

print(f'\n상위 {topN}을 시각화해봅니다.')

for (idx, prob_list) in enumerate(probability):
    plt.figure(figsize=(10, 8))

    captions = [item[1] for item in prob_list] # x축에 보여줄 class 이름
    data = [100.0 * item[2] for item in prob_list] # 그리고자 하는 확률

    chartdata = Series(data, index=captions)
    chartdata.plot(kind='bar', rot=12)

    plt.title(f'이미지 {file_list[idx]} 분류 결과', size=16)
    plt.grid(True)
    plt.ylim([-10, 100]) # 확률 값의 상하한 값

    filename = 'probability_' + file_list[idx]
    plt.savefig(image_destination + filename)
    print(f'{filename} 파일이 저장되었습니다.')
# end for









