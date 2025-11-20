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
newProduct = '망고에이드'

if boolean:
    print(f'가격이 {price}원인 상품이 존재합니다.')
else:
    print(f'{price}원인 상품인 {newProduct}을(를) 추가하였습니다.')
    coffeeList [newProduct] = price

print(coffeeList)

coffeeList2 = ['바닐라라떼','라벤더','딸기라떼','콜드브루']
price = 6000

for item in coffeeList2:
    price = price + 1000
    coffeeList [item] = price

print(coffeeList)

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
