import os
import pandas as pd

from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

dataIn = './../dataIn/'

# 코엔엘파이(konlpy)가 자바 경로를 찾습니다.
# 설정할 JAVA_HOME 경로
java_home_path = r'C:\Program Files\Java\jdk-12.0.2\bin'

# 환경 변수 설정
os.environ["JAVA_HOME"] = java_home_path

# 환경 변수 확인
print("JAVA_HOME is set to:", os.environ["JAVA_HOME"])

sample = '오늘 일정을 확인해 주세요.'

okt = Okt()
result = okt.morphs(sample)
print('형태소는 더 이상 분리할 수 없는 가장 작은 의미의 단위')
print('형태소 각각을 토큰(token)이라고 부릅니다')
print(f'형태소 분석 결과 : {result}')
print(f'문자열 결합 : {" ".join(result)}')

def tokenize(text):
    return ' '.join(okt.morphs(text))
# end def

email = '한정 수량! 지금 바로 클릭하세요'
result = tokenize(email)
print(f'형태소 분석 결과 : {result}')

print('\n분석에 사용할 email 목록 파일을 읽어 옵니다.')
email_frame = pd.read_csv(dataIn + 'mailList.csv')
email_frame.columns = ['메일 제목', '스팸 여부']

print('데이터 일부 확인')
print(email_frame.head())

print('\n메일 제목 token으로 만들기')
num_to_show = 5 # 보열줄 데이터 갯수

print('\n변수 emails는 메일의 제목과 스팸 여부를 tuple 형식으로 가지고 있는 list입니다.')
emails = [tuple(row) for row in email_frame.itertuples(index=False)]
print(emails[0:num_to_show])

print('\n변수 emails_tokenized는 메일의 제목이 토큰화 된 데이터입니다.')
print('변수 subject는 이메일 제목, label는 스팸 여부 문자열입니다.')
emails_tokenized = [(tokenize(subject), label) for subject, label in emails]
print(emails_tokenized[0:num_to_show])

print('\n독립 변수와 종속 변수로 분리합니다.')
x, y = zip(*emails_tokenized)

print(f'독립 변수(메일 제목) {num_to_show}개 보기')
print(x[0:num_to_show])

print(f'\n종속 변수(스팸 여부) {num_to_show}개 보기')
print(y[0:num_to_show])

print('\n머신 러닝에 사용하기 위하여 문자를 숫자화 시킵니다.')
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(x)
print(type(x))

# <Compressed Sparse Row sparse matrix of dtype 'int64'
# 	with 439 stored elements and shape (86, 139)>
#   Coords	Values
#   (0, 107)	1 <-- 0번째 문서에서 107에 해당하는 단어가 1번 나왔습니다.
#   (0, 43)	1 <-- 0번째 문서에서 43에 해당하는 단어가 1번 나왔습니다.

print(f'문서(이메일 제목)의 갯수는 {x.shape[0]}이고, 출현한 단어의 갯수는 {x.shape[1]}개입니다.\n')

vocab = vectorizer.vocabulary_
# dict comprehension : 역매핑(숫자 -> 단어)
inv_vocab = {v : k for k, v in vocab.items()}

su_list = [107, 43, 1]
for su in su_list:
    print(f'\'{su}\'번에 해당하는 단어 : {inv_vocab[su]}')
# end for

print('\n학습용 데이터와 테스트용 데이터를 분리 시킵니다.')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print('학습용 독립 변수 정보')
print(x_train[0:num_to_show])

print('\n학습용 종속 변수 정보')
print(y_train[0:num_to_show])

# MultinomialNB : 범주형 데이터에 사용하는 나이브 베이즈 클래스
# 베이즈 정리 : 조건부 확률에 기반한 ...
print('\n모델 생성')
model = MultinomialNB()

model.fit(x_train, y_train) # 학습 시킴

print('\n실제 값(actual)')
print(y_test) # 실제 정답을 의미하며, 머신 러닝에서 label이라고 부릅니다.

print('\n예측 값(predicted)')
prediction = model.predict(x_test) # 내가 작성한 답지
print(prediction)

print('\n각 클래스에 대한 확률 정보 확인')
prediction_proba = model.predict_proba(x_test)
print(prediction_proba) # 내부에서는 확률로 처리함

print('\n새로운 메일에 대하여 어떠한 유형의 메일인지 분류합니다.')
check_file = open(dataIn + 'checkedMail.csv', 'rt', encoding='utf-8')
test_mail_list = [onemail.strip() for onemail in check_file.readlines()]

print('\n점검하고 싶은 메일 목록')
print(test_mail_list)

print('\n각 메일을 반복하여 스팸 여부를 체크합니다.')
final_email_info = [] # 최종 결과를 저장할 리스트

for new_email in test_mail_list:
    new_email_tokenized = tokenize(new_email) # 토큰화
    new_email_vec = vectorizer.transform([new_email_tokenized]) # 벡터화

    prediction = model.predict(new_email_vec) # 모델을 이용하여 예측

    result = f"'{prediction[0]}' 메일 : '{new_email}'"
    print(result) # 결과 출력

    final_email_info.append(result)
# end for

print('\n최종 결과물')
print(final_email_info)