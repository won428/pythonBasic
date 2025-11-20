coffeeList01 = ('아메키라노','카페라떼')
coffeeList02 = ('콜드브루','아이스커피')

# 소괄호 없이 적어도 tuple이다.
coffeeList03 = '카푸치노','마키야또'

print(f'자료형 타입 : {type(coffeeList01)}')

# tuple, list로 형변환 가능 (양방향)
mylist = ['바닐라라떼', '플랫화이트']
coffeeList04 = tuple(mylist)

# 1번째 요소를 '고구마라떼'로 변경해보세요
change = list(coffeeList01)
change[0] = '고구마라떼'
coffeeList01 = tuple(change)
print(coffeeList01)

coffeeList = coffeeList01 + coffeeList02 + coffeeList03 + coffeeList04 + ('에스프레소',) # tuple로 인식하게 하려면 ,을 붙여야합니다.

length = len(coffeeList)
print(coffeeList)
print(f'요소 갯수 : {length}')

# 인덱싱 (정순은 0 베이스, 역순은 1베이스)
print(f'앞에서 2번 : {coffeeList[1]}')
print(f'뒤에서 1번: {coffeeList[-1]}')
# 슬라이싱
# coffeeList[start:end:step] : start부터 시작하여 end 직전까지 step 단계씩 슬라이싱 하세요
print(f'2-4번: {coffeeList[1:4]}')
print(f'4번 이상: {coffeeList[3:]}')
print(f'4번 이하: {coffeeList[:4]}')

print(f'홀수 : {coffeeList[0::2]}')
print(f'짝수 : {coffeeList[1::2]}')
print(f'전부 : {coffeeList[::]}')

myCount = coffeeList.count('고구마라떼')
print(f'고구마라떼의 개수 : {myCount}')
myIndex = coffeeList.index('콜드브루')
print(f'콜드브루의 인덱스 : {myIndex}')
