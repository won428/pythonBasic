import re

print('(1) split 함수 : 정규식 패턴을 사용하여 문자열을 분리합니다.')
mystring01 = '아메리카노,카페라떼:카푸치노 모카'
regEx = '[, :]' # 열거한 항목들을 모두 구분자로 사용함
pattern  = re.compile(regEx)
result = pattern.split(mystring01)
print(result)

print('\n(2) sub 함수 : 패턴과 일치하는 문자열을 대체(substitute)합니다.')
print('하이폰(-)을 슬래시(/)로 대체 합니다.')
mystring02 = '커피 생산일 : 2025-11-27'
regEx = '-' # 대상 문자열
pattern  = re.compile(regEx)
result = pattern.sub('/',mystring02) # sub(바뀔 문자열, 문자열 전체대상)
print(result)

print('(3) subn 함수 : 패턴과 일치하는 문자열을 n개만 대체합니다. ')
mystring03 = '01-02-03-04-05'
regEx = '-' # 대상 문자열
pattern  = re.compile(regEx)

print(f'원본 문자열 : {mystring03}')
for idx in range(1, 5):
    result = pattern.subn('/', mystring03, idx)
    print(f'count : {idx} → {result[0]}')

