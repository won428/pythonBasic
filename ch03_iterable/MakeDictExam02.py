breads = {'바게트' : 100, '치아바타' : 200, '호밀빵' : 300, '베이글' : 400}
findData = '스콘'
boolean = findData in breads

if not boolean:
    breads [findData] = 150

breads ['치아바타'] = 250
price = 300

if not price in breads.values():
    breads ['브리오슈'] = price

newItems = ['통밀빵', '옥수수빵', '크랜베리빵']

price = 400
for item in newItems:
    price = price + 100
    breads [item] = price

targetList = ['옥수수빵', '단팥빵']
for item in targetList:
    try:
        print(f'품목 : {item}, 가격 : {breads[item]}')
    except KeyError:
        print(f'{item}은 없는 품목 입니다.')

print(breads)