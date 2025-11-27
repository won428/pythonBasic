import re

mystring = '오늘은 2025년 11월 입니다.'
regEx = '\d+' # 숫자가 1개 이상 이어야 합니다.
pattern = re.compile(regEx)

result = pattern.match(mystring)
print('match 함수는 문자열의 처음부터 체크합니다.')
print(f'match 결과 : {result}')

result = pattern.search(mystring)
print('search 함수는 임의의 위치에서 조건에 맞으면 출력해 줍니다.')
print(f'search 결과 : {result}')

print('\n특정 문자로 시작하는 데이터 찾기')
mylist01 = ['hello123', 'world99']
regEx = '^h[a-z]*' # h로 시작하는 항목들
pattern = re.compile(regEx)

print('match 함수 실행결과')
for item in mylist01:
    if pattern.match(item):
        print(f'{item} : True')
    else:
        print(f'{item} : False')
# end for

print('search 함수 실행결과')
for item in mylist01:
    if pattern.search(item):
        print(f'{item} : True')
    else:
        print(f'{item} : False')
# end for

print('위 예제에서 match 함수와 search 함수의 실행 결과는 동일합니다.')
print('\nmatch 함수의 반환 결과는 Match 객체입니다.')
print('\nMatch 객체는 색인이나 위치, 문자열 정보를 위한 여러개의 메소드가 존재합니다.')
mystring = 'python1234'
regEx = '[a-z]+' # 알파벳이 1번 이상 나오기
pattern = re.compile(regEx)
result = pattern.match(mystring)
print(type(result))

start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {mystring[start_idx:end_idx]}')

print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {result.start()}')
print(f'문자열 끝 인덱스 : {result.end()}')
print(f'문자열 색인 tuple 정보 : {result.span()}')

print('\nsearch 함수의 반환 결과 역시 Match 객체입니다.')
newstring = '2026 worldcup'
regEx = '[a-z]+' # 알파벳이 1번 이상 나오기
pattern = re.compile(regEx)
result = pattern.search(newstring)
print(type(result))

start_idx, end_idx = result.start(), result.end()

print(f'슬라이싱 : {newstring[start_idx:end_idx]}')

print(f'조건에 맞는 문자열 : {result.group()}')
print(f'문자열 시작 인덱스 : {result.start()}')
print(f'문자열 끝 인덱스 : {result.end()}')
print(f'문자열 색인 tuple 정보 : {result.span()}')

addressList = ["('강원원주시웅비2길8');",
          "('강원도철원군서면와수로181번길7-16');",
          "('강원평창군봉평면태기로68');",
          "('강원강릉시강변로410번길36');"]
regEx = r'\d\S*\'' # 숫자로 시작 이후에 white character 문자가 아닌것 들을 말합니다.
pattern = re.compile(regEx)
for address in addressList:
    mymatch = pattern.search(address)
    print(mymatch.group().rstrip("'")) # 우측 외따옴표 지우기
# end for