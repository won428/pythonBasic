import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # 아래 경고 메시지 때문에 작성해줌
# 2025-12-11 18:01:07.916279: I tensorflow/core/util/port.cc:153] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
# 2025-12-11 18:01:10.574809: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
# To enable the following instructions: SSE3 SSE4.1 SSE4.2 AVX AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Model
from keras.src.applications.vgg16 import VGG16, preprocess_input
from keras.src.layers import GlobalAveragePooling2D, Dense, Dropout
from keras.src.utils import load_img, img_to_array
from pandas import Series

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

IMAGE_WIDTH, IMAGE_HEIGHT = 224, 224 # VGG16 모델의 이미지 사이즈 정보
image_source = './../dataIn/image/' # 이미지를 읽어 들일 경로
image_destination = './../dataOut/' # 이미지 파일이 저장될 경로

# VGG16 로드
# weights : ImageNet 데이터 셋에서 학습했던 모델 정보를 그대로 사용하겠습니다.
# include_top=False : 1000개의 클래스를 무시하고, 내가 10개로 하겟습니다.
# input_shape : 입력 이미지 크기를 지정하는 부분
model = VGG16(weights='imagenet', include_top=False, input_shape=(IMAGE_WIDTH, IMAGE_HEIGHT, 3))

model.trainable = False # 사전 학습 모델 정보는 다시 내가 학습시키지 않겠습니다.
# 다만 우리가 다시 추가하는 Dense 층들만 학습시킬께요.

# Custom classifier 생성
x = model.output
x = GlobalAveragePooling2D()(x) # GlobalAveragePooling2D(전역 평균 풀링)은 CNN의 마지막 Feature Map을 하나의 벡터로 변환하는 층입니다.
x = Dense(256, activation='relu')(x)
x = Dropout(0.5)(x)
x = Dense(128, activation='relu')(x)

outputs = Dense(10, activation='softmax')
model = Model(inputs=model.input, outputs=outputs(x))

# loss : 손실 함수, optimizer : 최적화 알고리즘, metrics : 평가 지표
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 이미지 로딩
file_list = os.listdir(image_source)
total_data = []

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
    pre_input = preprocess_input(ndarray)
    total_data.append(pre_input)
# end for (file_list loop)

x_train = np.stack(total_data)

# Fine-tuning 레이어 지정
for layer in model.layers[-4:]:
    layer.trainable = True
# end for (trainable layer loop)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 예측
prediction = model.predict(x_train)

# probability 리스트 생성
probability = []
topN = 5

for pred_idx, pred in enumerate(prediction):
    top_idx = pred.argsort()[::-1][:topN]
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
