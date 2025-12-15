'''
관련 파일
    윤석열 제20대 대통령 취임사.txt
    user_dic.txt
    stopword.txt
    alice_color.png

설치할 라이브러리
    pip install konlpy <- 한글 형태소 분석 라이브러리
    pip install nltk <- 자연어 처리 툴킷
    pip install wordcloud <- 워드 클라우드
'''
# nltk : National Language ToolKit
import nltk
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='Malgun Gothic')

# opencv 라이브러리도 같이 공부할 것
from PIL import Image # Python Image Library
from wordcloud import WordCloud
# ImageColorGenerator : 컬러 이미지의 색상 톤을 유지하면서 워드 클라우드를 사용하고자 할때 사용합니다.
from wordcloud import ImageColorGenerator
from konlpy.tag import Komoran

# 코엔엘파이(konlpy)가 자바 경로를 찾습니다.
# 설정할 JAVA_HOME 경로
java_home_path = r'C:\Program Files\Java\jdk-12.0.2\bin'

# 환경 변수 설정
os.environ["JAVA_HOME"] = java_home_path

# 환경 변수 확인
print("JAVA_HOME is set to:", os.environ["JAVA_HOME"])

dataIn = './../dataIn/'
dataOut = './../dataOut/'
filename = dataIn + '윤석열 제20대 대통령 취임사.txt'

speech = open(filename, 'rt', encoding='utf-8').read()
# print(speech)

user_dict = dataIn + 'user_dic.txt'

komo = Komoran(userdic=user_dict) # 형태소 분석 객체

token_list = komo.nouns(speech) # 명사만 추출
print(f'\n토큰 개수 : {len(token_list)}')
# print(f'토큰 목록')
# print(token_list)

stopword_file = dataIn + 'stopword.txt'
stop_file = open(stopword_file, 'rt', encoding='utf-8').readlines()
stop_words = [word.strip() for word in stop_file]
print('\n불용어 목록')
print(stop_words)

print('\n불용어를 제외한 토큰 목록')
new_token_list = [word for word in token_list if word not in stop_words]
print(new_token_list)

bindo_size = 500 # 빈도 수
print(f'\n단어들의 빈도 수를 내림차순 정렬하여 상위 {bindo_size}개만 추출합니다.')
nltk_token = nltk.Text(tokens = new_token_list)
token_data = nltk_token.vocab().most_common(n = bindo_size)

print('토큰과 빈도 수 확인')
print(token_data)

print('\n단어들과 빈도 수를 위한 리스트를 생성합니다.')
print('단어의 길이가 2이상이고, 빈도의 수가 2이상인 항목들만 추출합니다.')
wordList = list()

for word, bindo in token_data:
    if len(word) >= 2 and bindo >= 2:
        wordList.append((word, bindo))
    # end if
# end for

print(wordList)

word_frame = pd.DataFrame(wordList, columns = ['단어', '빈도수'])
print(word_frame.head())

barCount = 10 # 그리고자 하는 막대의 갯수
print(f'\n상위 top {barCount}개 막대 그래프')
chart_data = word_frame.set_index('단어').iloc[:barCount]

chart_data.plot(kind='bar', rot=10, grid=True, legend=False)
plt.title(f'빈도 : {barCount} 개 상위 단어', size=18)
plt.xlabel('주요 키워드', size=12)
plt.ylabel('빈도수', size=12)

filename = dataOut + 'bar_chart.png'
plt.savefig(filename)
print(f'{filename} 파일 저장됨')

print('\n단어의 빈도 수를 이용한 워드 클라우드')
alice_color_filename = dataIn + 'alice_color.png'
alice_color_array = np.array(Image.open(alice_color_filename)) # 이미지 배열


fontName = 'malgun.ttf' # 글꼴

wordDict = dict(wordList) # 단어 사전 : 워드 클라우드에 반드시 사전 형식으로 넣어 주어야 합니다.

# alice_word_cloud : 워드 클라우드 객체
alice_word_cloud = WordCloud(background_color='white', font_path=fontName, mask=alice_color_array)

# 사전 정보를 이용하여 빈도수를 생성합니다.
alice_word_cloud = alice_word_cloud.generate_from_frequencies(wordDict)

# 컬러 색상 톤을 그대로 유지하고자 할 때 사용하는 제너레이터입니다.
color_generator = ImageColorGenerator(alice_color_array)

alice_word_cloud = alice_word_cloud.recolor(color_func = color_generator)

plt.figure(figsize=(16, 8))
plt.axis('off') # 그래프 테두리 없애기
plt.imshow(alice_word_cloud)

cloudFileName = dataOut + 'alice_word_cloud.png'
plt.savefig(cloudFileName)
print(f'{filename} 파일 저장됨')



