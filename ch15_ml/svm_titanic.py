import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.svm import SVC

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 글자 깨짐 방지

# metrics : 평가 지표
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


dataOut = './../dataOut/'

# 타이타닉 데이터
df = sns.load_dataset('titanic')
print(f'데이터 타입 : {type(df)}')
print(f'컬럼 정보 : {df.columns}')

print(f'\n지도 학습법 : 문제지와 답지를 같이 나눠주고, 분석을 예측하는 기법')
print(f'타이타닉은 나머지 컬럼을 입력으로, "survived" 컬럼을 예측하는 분류 문제입니다.')

print(f'\n일부 데이터 확인')
print(df.head())

print(f'\n항목별 빈도수')
survived_counts = df['survived'].value_counts()
survived_counts.index = survived_counts.index.map({0: '사망', 1: '생존'})
print(survived_counts)

print(f'\n이 모델은 클래스의 갯수가 {len(survived_counts)}개입니다.')

print(f'\n중복되는 행 개수 : {sum(df.duplicated())}개입니다.')
print(f'before drop duplicated : {len(df)}개입니다.')
df = df.drop_duplicates()
print(f'after drop duplicated : {len(df)}개입니다.')

print(f'\n데이터 프레임 정보 확인하기')
print(df.info())

print(f'\n관심 컬럼 확인')
print(df[['embarked', 'embark_town']].head(10))

print(f'\n결측치가 많은 "deck"와 의미가 중복이 되는 "embark_town" 컬럼은 삭제합니다.')
dropnadf = df.drop(['deck', 'embark_town'], axis=1)

print(f'\n나이 컬럼에 결측치가 있으면 제거합니다.')
# how='any' 옵션은 행 또는 열에 결측치가 1개 이상이면 제거시킵니다.
dropnadf = dropnadf.dropna(subset=['age'], how='any', axis=0)

print(f'\n승선 위치 범주 데이터 : {df["embarked"].unique()}') # ['S' 'C' 'Q' nan]
print('승선 위치 컬럼의 결측치(nan)는 빈도 수가 가장 많은 항목으로 대체합니다.')
print('항목별 빈도 수')
print(df["embarked"].value_counts())

# mode() 함수는 빈도 수를 내림 차순으로 정렬해주는 함수입니다.
most_frequency = dropnadf["embarked"].mode()[0]
print(f'승선 위치 컬럼에서 가장 빈도가 큰 항목 : {most_frequency}')
print(f'컬럼 embarked의 결측치를 {most_frequency} 값으로 채워 줍니다.')
dropnadf["embarked"] = dropnadf["embarked"].fillna(most_frequency)

print(f'\n머신 러닝 분석에서 사용되는 column을 특성(Feature)라고 부릅니다.')
print(f'분석에 사용할 열(특성) 선택')
newframe = dropnadf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(newframe.columns)

print(f'\n데이터 일부분 확인')
print(newframe.head())

print(f'\n범주형 데이터 전처리 : one-hot encoding')
# 범주형 데이터를 머신 러닝 모델이 인식할 수 있도록 숫자 형식으로 변환해 줍니다.
onehot_sex = pd.get_dummies(data=newframe['sex'], dtype=int)
onehot_embarked = pd.get_dummies(data=newframe['embarked'], prefix='town', dtype=int)
newframe = pd.concat([newframe, onehot_sex, onehot_embarked], axis=1)

print(f'\nsex, embarked 컬럼 삭제')
newframe = newframe.drop(['sex', 'embarked'], axis=1)

print(f'\n최종 데이터 일부분 확인')
print(newframe.head())
print(f'컬럼 정보 : {newframe.columns}')

print('\n# 독립 변수 : 분석에 영향을 미치는 변수(input 데이터 : 문제지)')
print('# 종속 변수 : 독립 변수에 의하여 영향을 반는 변수(output 데이터 : 답지)')
print('# 독립 변수와 종속 변수 분리')

x = newframe[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']]
y = newframe['survived']

print('\nbefore normalization')
print(x[:5])

# svm, knn 등의 알고리즘은 거리 기반으로 계산합니다.
# 반드시, 정규화가 필요합니다.
# 정규화는 훈련용 데이터에만 반영하도록 합니다.
scaler = StandardScaler()
x = scaler.fit(x).transform(x)

print('\nafter normalization')
print(x[:5])

print('\n학습용 데이터와 테스트용 데이터로 분리')
# random_state=10 옵션은 랜덤값 시드 배정
x_train, x_test, y_train, y_test = \
    train_test_split(x, y, test_size=0.3, random_state=10)

# 모델 생성
model = SVC(kernel='rbf', probability=True)

# fit() 함수를 해당 모델을 훈련시켜 주는 함수입니다.
model.fit(x_train, y_train) # 내가 공부할 시험지와 답지

print('\n# predict() 함수는 가장 높은 확률의 클래스 값(0 또는 1)을 반환해 줍니다.')
prediction = model.predict(x_test) # x_test는 답지 없이 시험본 나의 문제지

print('# 예측 값(모의 고사에서 내가 작성한 답지)')
print(prediction[0:10])

print('\n# 실제 정답 데이터(모의 고사의 진짜 답지_label)')
print(y_test.values[0:10])

print('\n# 예측 값과 실제 값을 하나의 DataFrame으로 만들기')
result_df = pd.DataFrame({
    'actual': y_test.values, # 실제 정답
    'predicted': prediction, # 예측 값
    'correct': y_test.values == prediction # 맞았으면 True
})

csv_filename = dataOut + 'titanic_svm_predict.csv'
result_df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

print('\n# 분류 모델 성능 평가')
print('# confusion_matrix(실제정답데이터, 예측값)')
svm_matrix = confusion_matrix(y_test, prediction)
print(svm_matrix)

print('\n# confusion_matrix 시각화')
plt.figure(figsize=(8, 6))
sns.heatmap(svm_matrix, annot=True, cmap='Blues', fmt='d',
            xticklabels=['사망', '생존'],
            yticklabels=['사망', '생존'])

plt.title('Confusion Matrix')
plt.ylabel('실제값')
plt.xlabel('예측값')

filename = dataOut + 'svm_titanic_image_01.png'
plt.savefig(filename)
print(f'{filename} 파일이 저장되었습니다.')

print('\n# 분류 보고서(classification_report)')
svm_report = classification_report(y_test, prediction)
print(svm_report)

# predict_proba 함수는 각 클래스에 대한 확률 정보를 반환해 줍니다.
# 이 예시는 클래스 갯수 2개이므로 예를 들면 [0.35, 0.65]의 형식으로 반환해 줍니다.
prediction_probability = model.predict_proba(x_test)
print(prediction_probability[0:3])

# 생존일 확률 정보만 따로 추출합니다.
alive_probability = prediction_probability[:, 1]

# ROC 커브 그리기
fpr, tpr, thresholds = roc_curve(y_test, alive_probability)

roc_auc = auc(fpr, tpr)

# ROC 커브 시각화
plt.figure(figsize=(8, 8))

plt.plot(fpr, tpr, color='darkorange', lw = 2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw = 2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.title('ROC curve')
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.legend(loc="lower right")

filename = dataOut + 'svm_titanic_roc_curve.png'
plt.savefig(filename)
print(f'{filename} 파일이 저장되었습니다.')