# SomeBuiltIn01.py
print('list에 대한 집계 함수 적용')
mylist = [10, 90, 50]
print('sum(mylist) : %d' % sum(mylist))
print('min(mylist) : %d' % min(mylist))
print('max(mylist) : %d' % max(mylist))

print('\ntuple에 대한 집계 함수 적용')
mytuple = (10, 90, 50)
print('sum(mytuple) : %d' % sum(mytuple))
print('min(mytuple) : %d' % min(mytuple))
print('max(mytuple) : %d' % max(mytuple))

print('\nset에 대한 집계 함수 적용')
myset = {10, 90, 50}
print('sum(myset) : %d' % sum(myset))
print('min(myset) : %d' % min(myset))
print('max(myset) : %d' % max(myset))

# 특정 문자열 내의 글자들을 중복되지 않게 집합으로 만들어 봅니다.
# list 컴프리헨션 기능을 이용하여 list 형식으로 변경한 뒤 정렬합니다.
mystring = 'hello'
myset = set(mystring)
print(myset)

result = [item for item in myset]
result.sort() # 오름차순 정렬
print(result)

# ord() 함수는 특정 글자를 ascii 코드로 변경해 줍니다.
result = [ord(item) for item in myset]
result.sort() # 오름차순 정렬
print(result)

print('bin(8) :', bin(8))
print('oct(10) :', oct(10))
print('hex(20) :', hex(20))
print('int(34.56) :', int(34.56))
print('float(12) :', float(12))
print('월드컵 2002 :', '월드컵 ', str(2002))
print('eval(\'3+5\') :', eval('3+5'))
print('round(45.67) :', round(45.67))

# chr(아스키코드) 함수는 ascii 코드를 문자열로 변경
print('chr(65) :', chr(65))
print('pow(2, 10) :', pow(2, 10))

# 프로그래밍에서 숫자 0은 거짓, 1은 참으로 인식합니다.
mylist = [False, 1, False]
# 모든 요소가 참인가요?
print('all(mylist) :', all(mylist))

# 참인 요소가 적어도 1개 이상 있나요?
print('any(mylist) :', any(mylist))

mylist = [1, 2, 3, 4, 5, 6]
print('모든 숫자가 4보다 작습니까?', all(idx < 4 for idx in mylist))
print('숫자 4보다 작은 항목이 있나요?', any(idx < 4 for idx in mylist))