# 다음 리스트의 모든 요소들을 반복문을 사용하여 총합을 구해 보되, range 함수를 사용하는 방식과 사용하지 않는 두 가지 방식을 사용하여 풀어 보세요.
# 단, 요소의 값이 음수인 항목은 절대 값으로 변경하여야 합니다.
mylist = [10, -20, 30, -40, 50]

sum01 = 0
for number in mylist:
    if number < 0:
        number = abs(number)
    sum01 += number
# end for
print(sum01)

sum02 = 0
for i in range(len(mylist)):
    if mylist[i] < 0:
        mylist[i] = abs(mylist[i])
    sum02 += mylist[i]
# end for
print(sum02)

# sum 집계 함수를 이용하여 다시 풀어 보세요.
sum03 = sum(abs(n) for n in mylist)
print(sum03)
