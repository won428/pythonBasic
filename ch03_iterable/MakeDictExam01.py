coffeeList = dict() # {기호도 가능}
coffeeList ['에스프레소'] = 1000 # 신규 추가
coffeeList ['에스프레소'] = 1500 # 이미 존재하면 덮어 쓰기

coffeeList ['카페라떼'] = 2000
coffeeList ['카푸치노'] = 3000
coffeeList ['마키야또'] = 4000

findData = '카페라떼'
boolean = findData in coffeeList

if boolean:
    print(f'키 {findData}이(가) 존재합니다.')
else:
    print(f'{findData}은(는) 존재하지 않습니다.')

print(coffeeList)
print(type(coffeeList))
print(f'요소 개수 : {len(coffeeList)}')

findData = '핫초코'
boolean = findData in coffeeList

if not boolean:
    print(f'{findData}을(를) 추가했습니다.')
    coffeeList ['핫초코'] = 5000
else:
    print('존재하는 데이터 입니다')

print(f'키 목록 : {coffeeList.keys()}')
print(f'값 목록 : {coffeeList.values()}')
print(coffeeList)

price = 6000
boolean = price in coffeeList.values()
newProduct = '아이스커피'

if boolean:
    print(f'가격이 {price}원인 상품이 존재합니다.')
else:
    print(f'{price}원인 상품인 {newProduct}을(를) 추가하였습니다.')
    coffeeList [newProduct] = price


coffeeList2 = ['바닐라라떼','라벤더','딸기라떼','콜드브루']
price = 6000

for item in coffeeList2:
    price = price + 1000
    coffeeList [item] = price


findData = '핫초코'
print(f'{findData}의 가격은 {coffeeList[findData]}입니다.')

tagetList = ['라벤더','우유커피']

for item in tagetList:
    try:
        print(f'품명 : {item}, 가격 : {coffeeList[item]}')
    except KeyError:
        print(f'{item}은(는) 존재하지 않는 품목입니다.')

findData = '둥글레차'
price = coffeeList.get(findData, 3000) # 없으면 기본값으로
print(f'품명 : {findData}, 가격 : {price}')

findData = '아이스커피'
popItem = coffeeList.pop(findData)
message = f'삭제된 품목 {findData}의 가격은 {popItem}원 입니다.'
print(message)

del coffeeList['에스프레소'] # coffeeList dict에서 '에스프레소' 삭제

# dict의 keys와 values를 각각 tuple의 형태로 묶어 반환합니다.
# 변수를 밑처럼 두개 입력하면 각각 [0], [1]이 파이썬이 할당 해주므로 key와 value가 들어갑니다.
for (key, value) in coffeeList.items():
    message = f'품목 {key}의 단가는 {value}원 입니다.'


# 전체목록 출력
# 단, '카페라떼와 '카푸치노'는 500원 인상
# '핫초코'는 500원 인하
# 파이썬에서 else는 빈값으로 둘 수 없습니다. 빈값으로 둬야하는 경우는 pass를 사용합니다.
for key in coffeeList.keys():
    if key == '카페라떼' or key == '카푸치노':
        coffeeList[key] = coffeeList[key] + 500
    elif key == '핫초코':
        coffeeList[key] = coffeeList[key] - 500
    else:
        pass
    # end if
    message = f'품명 : {key}, 가격 : {coffeeList[key]}'
    print(message)
# end for

coffeeList.clear()

if len(coffeeList) == 0:
    print('my dict is empty')
else:
    print('my dict is not empty')
# end if

print(coffeeList)