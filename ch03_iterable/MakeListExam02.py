# coffeeList = [] # empty list
coffeeList = list() # 함수를 이용한 빈 리스트 생성

coffeeList.append('아메리카노')
coffeeList.append('콜드브루')
coffeeList.append('카푸치노')
coffeeList.append('바닐라라떼')
coffeeList.append('디카페인 커피')
coffeeList.append('카페라떼')

count = len(coffeeList)
print(f'요소 개수 : {count}')

# 인덱싱 (정순은 0 베이스, 역순은 1베이스)
print(f'앞에서 2번 : {coffeeList[1]}')
print(f'뒤에서 1번: {coffeeList[-1]}')
# 슬라이싱
# coffeeList[start:end:step] : start부터 시작하여 end 직전까지 step 단계씩 슬라이싱 하세요
print(f'2-4번: {coffeeList[1:4]}')
print(f'4번 이상: {coffeeList[3:]}')
print(f'4번 이하: {coffeeList[:4]}')

coffeeList[0] = '고구마라떼'

print(f'홀수 : {coffeeList[0::2]}')
print(f'짝수 : {coffeeList[1::2]}')
print(f'전부 : {coffeeList[::]}')

print('오름차순 정렬')
coffeeList.sort()
print(coffeeList)

print('내림차순 정렬')
coffeeList.sort(reverse=True)
print(coffeeList)

