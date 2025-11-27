import re

print('===== 커피 데이터에서 숫자 찾기 =====')
coffee_info = '아메리카노 3500원입니다.'
regEx = '\d+'  # 숫자가 1개 이상
pattern = re.compile(regEx)
result = pattern.search(coffee_info)
print(result.group())
# match와 search 함수 테스트


print('\n===== 특정 단어로 시작하는 커피 이름 찾기 =====')
coffee_list = ['latte123', 'mocha99', 'latte_special']
regEx = '^latte'   # latte로 시작하는 항목들
pattern = re.compile(regEx)
latteList = list()
for coffee in coffee_list:
    result = pattern.match(coffee)
    if result:
        latteList.append(coffee)
print(latteList)


print('\n===== match 함수의 반환 결과는 Match 객체입니다. =====')
coffee_name = 'espresso_2500'
regEx = '([a-z_]+)'  # 알파벳 소문자 또는 _가 1번 이상
pattern = re.compile(regEx)
result = pattern.match(coffee_name)
start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {coffee_name[start_idx:end_idx]}')
print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {start_idx}')
print(f'문자열 끝 인덱스 : {end_idx}')
print(f'문자열 색인 tuple 정보 : {result.span()}')


print('\n===== search 함수의 반환 결과 역시 Match 객체입니다. =====')
order_info = '총 주문 금액은 4800원입니다.'
regEx = '\d+'  # 숫자 1번 이상
pattern = re.compile(regEx)
result = pattern.search(order_info)

start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {order_info[start_idx:end_idx]}')
print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {start_idx}')
print(f'문자열 끝 인덱스 : {end_idx}')
print(f'문자열 색인 tuple 정보 : {result.span()}')
