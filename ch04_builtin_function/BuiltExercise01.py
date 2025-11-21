coffees = ['바닐라라떼','카페라떼','고구마라떼']
price = [1000,2000,3000,4000]

# zip()
for item in zip(coffees, price):
    print(item)

myList = list(zip(coffees, price))
print(myList)
myDict = dict(zip(coffees, price))
print(myDict)

# sorted()
print('\nkey를 사용한 오름차순 정렬')
result = sorted(myDict.keys())
print(result)
print('key를 사용한 내림차순 정렬')
result = sorted(myDict.keys(), reverse= True)
print(result)

print('\nvalue를 사용한 오름차순 정렬')
result = sorted(myDict.values())
print(result)
print('value를 사용한 내림차순 정렬')
result = sorted(myDict.values(), reverse= True)
print(result)

print('\nvalue를 기준으로 내림차순 정렬하되, 품목 이름 출력')
result = sorted(myDict, key=myDict.get, reverse=True)
print(result)

print('\nitems를 사용한 key 오름차순 정렬')
result = sorted(myDict.items())
print(result)
print('items를 사용한 key 내림차순 정렬')
result = sorted(myDict.items(), reverse= True)
print(result)

print('\nitems를 사용한 value 오름차순 정렬')
result = sorted(myDict.items(), key= lambda x:x[1])
print(result)
print('items를 사용한 value 내림차순 정렬')
result = sorted(myDict.items(), reverse= True)
print(result)



# 다음 리스트를 사용하여 물음에 답해 보세요.
human = ['김철수', '홍길동', '박영희']
jumsu = [50, 60, 70]
# zip() 함수를 사용하여, 다음과 같은 데이터 mylist를 만드세요.

zipList = list(zip(human,jumsu))
print(zipList)
mylist = [('김철수', 50), ('홍길동', 60), ('박영희', 70)]

# mylist를 사전 mydict으로 변경해 보세요.(dict() 함수 적절히 사용)
mydict = dict(mylist)
print(mydict)

# mydict를 이용하여 점수가 높은 사람 순부터 '이름'을 출력해 보세요.(sorted() 함수)
result = sorted(mydict, key=mydict.get, reverse= True)
print(result)