# 다음 리스트의 요소 중에서 최소 값, 최대 값, 평균 값을 요소로 하는 신규 튜플을 생성하는 프로그램을 작성해 보세요.
mylist = [10, 20, 30, 40]
sum = sum(mylist)
min = min(mylist)
max = max(mylist)
avg = sum / len(mylist)

newList = (min, max, avg)
print(newList)