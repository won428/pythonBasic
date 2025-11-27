import re

from ch04_builtin_function.BuiltExercise01 import coffees

print('findall 함수는 정규식과 매치되는 모든 문자열을 list 형식으로 반환해 줍니다.')
mystring01 = '삼일절은 1919년 3월 1일입니다.'
print(mystring01)
regEx = '\d+'
pattern = re.compile(regEx)
result = pattern.findall(mystring01)
print(result)
message = f'삼일절 {result[0]}년 {result[1].zfill(2)}월 {result[2].zfill(2)}일'
print(message)

print('\n총 구매 수량 구하기')
mystring02 = '사과 5개, 밤 3개, 배 4개만 주문할게요'
print(mystring02)
regEx = '\d+'
pattern = re.compile(regEx)
result = pattern.findall(mystring02)
total = 0
for quantity in result:
    total += int(quantity)
# end for
print(f'총 구매 수량 : {total}\n')

print('b로 시작하는 단어들만 추출하기')
mystring03 = 'blow block 1234 peace blame 5678 blood'
regEx = 'b[a-z]*'
pattern = re.compile(regEx)
words = pattern.findall(mystring03)
words.sort()
print(f'{words}\n')

print('finditer 함수는 결과물을 반복이 가능한 개체 형식으로 반환해 줍니다.')
print('일반적으로 for 구문과 같이 사용합니다.')

words = pattern.finditer(mystring03)
for item in words:
    print(f'객체 정보 : {item}')
    print(f'문자열 정보 : {item.group()}')
    print(f'색인 위치 : {item.span()}')
    st_idx, end_idx = item.start(), item.end()
    print(f'슬라이싱 : {mystring03[st_idx:end_idx]}')

mystring04 = '사과 5개, 밤 3개, 배 4개만 주문할게요'
print(mystring04)
regEx = '\d개'
pattern = re.compile(regEx)
result = pattern.finditer(mystring04)
for item in result:
    print(item.group())

mystring05 = '아메리카노 2잔, 카페라떼 4잔'
regEx = '\d+'
pattern = re.compile(regEx)
coffees = pattern.finditer(mystring05)
total = 0
for coffee in coffees:
    total += int(coffee.group())



print(f'음료 구매 수량 : {total}')