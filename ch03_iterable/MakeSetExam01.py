from logging import exception

coffeeList = set()

# 중복 값은 하나만 들어간다.
coffeeList.add('아메리카노')
coffeeList.add(100)
coffeeList.add(True)
coffeeList.add('아메리카노')
# 전체삭제
coffeeList.clear()
# 항목 추가
coffeeList.add('아메리카노')
coffeeList.add('에스프레소')
coffeeList.add('믹스커피')
coffeeList.add('카페라떼')
# 추가할 새 상품
newItems = ['콜드브루', '고구마라떼', '디카페인커피']
# update , 집합에 새 상품 업데이트
coffeeList.update(newItems)

# 집합은 순서가 없으므로, 밑처럼 인덱싱/슬라이싱 불가능
# print(coffeeList[3])

findData = '카푸치노'
boolean = findData in coffeeList
print(f'{findData} 존재 여부 : {boolean}') # fstring

findData = '마키야또'
boolean = findData in coffeeList
if not findData in coffeeList:
    coffeeList.add(findData)
# end if

findData = '믹스커피'
coffeeList.remove(findData)

try:
    findData = '바닐라라떼'
    coffeeList.remove(findData)
except KeyError:
    print('없는 데이터')

# discard 메소드는 존재하지 않더라고 예외 없이 넘어갑니다.
coffeeList.discard('바닐라라떼')

# 집합은 순서가 없으므로, 어떤 데이터가 나올지는 예측할 수 없습니다.
popItem = coffeeList.pop()
print(f'pop()으로 제거된 요소 : {popItem}')

# print('반복문을 사용한 출력')
# for item in coffeeList:
#     print(item)
# end for



print(f'자료형 타입 : {type(coffeeList)} ')
print(f'요소 개수 : {len(coffeeList)}')
print(coffeeList)

print('집합 연산')

# set()은 빈 함수를 만들때 사용합니다. 밑에 두 방식으로 집합에 값을 추가할 수 있습니다.
store01 = set(['고구마라떼','에스프레소','아메리카노','마키야또'])
store02 = {'아메리카노','마키야또','카페라떼','디카페인커피'}
# 합집합
unionSet = store01.union(store02) # unionSet = store01 | store02 처럼 기호로도 합집합을 표현할 수 있습니다.
# 차집합
items01 = store01.difference(store02) # items01 = store01 - store02 처럼 기호로도 차집합을 표현할 수 있습니다.
items02 = store02 - store01
# 교집합
intersectionSet = store01.intersection(store02) # intersectionSet = store01 & store02 처럼 기호로도 교집합을 표현할 수 있습니다.

print(f'1번 매장 또는 2번 매장에서 구매 가능한 품목\n{unionSet}')
print(f'1번 매장에서만 구매 가능한 품목\n{items01}')
print(f'2번 매장에서만 구매 가능한 품목\n{items02}')
print(f'매장 공통으로 구매 가능한 품목\n{intersectionSet}')

# 각 집합의 고유 원소들의 합(symmetric_difference)
print('하나의 매장에서만 판매하는 품목들의 총합')
print(store01.symmetric_difference(store02)) # store01 ^ store02 처럼 기호로도 표현할 수 있습니다.

# 부분 집합
print('\n부분 집합')
super_set = {'고구마라떼','에스프레소','아메리카노','마키야또'}
sub_set_01 = {'아메리카노','마키야또'}
sub_set_02 = {'바닐라라떼','마키야또'}

# 하위집합 체크
boolean = sub_set_01.issubset(super_set)
if boolean:
    print(f'{sub_set_01}은 {super_set}의 부분 집합 입니다.')
else:
    print(f'{sub_set_01}은 {super_set}의 부분 집합이 아닙니다.')
# end if

boolean = sub_set_02.issubset(super_set)
if boolean:
    print(f'{sub_set_02}은 {super_set}의 부분 집합 입니다.')
else:
    print(f'{sub_set_02}은 {super_set}의 부분 집합이 아닙니다.')
# end if

# 상위집합 체크
boolean = super_set.issuperset(sub_set_01)
if boolean:
    print(f'\n{super_set}은 {sub_set_01}의 상위 집합 입니다.')
else:
    print(f'{super_set}은 {sub_set_01}의 상위 집합이 아닙니다.')
# end if

boolean = super_set.issuperset(sub_set_02)
if boolean:
    print(f'{super_set}은 {sub_set_02}의 상위 집합 입니다.')
else:
    print(f'{super_set}은 {sub_set_02}의 상위 집합이 아닙니다.')
# end if