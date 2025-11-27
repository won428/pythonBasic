import re
print('1) split 함수를 사용하여 데이터를 사전으로 변환하기')
mystring01 = '사과:10/오렌지:20/감:30/밤:40'
regEx = '[:/]'
pattern = re.compile(regEx)
result = pattern.split(mystring01)
print(result[0])
fruitDict = dict()
for i in range(0, len(result), 2):
    fruitDict[result[i]] = int(result[i+1])
# 리스트를 2개씩 묶어 사전으로 변환
print(fruitDict)

# 출력 예: {'사과': '10', '오렌지': '20', '감': '30', '밤': '40'}

print('\n2) sub 함수를 사용하여 -를 /로 변경하기')
mylist = ['광복절 : 1945-08-15', '삼일절 : 1919-03-01']

regEx = '-'
pattern = re.compile(regEx)
for item in mylist:
    new = pattern.sub('/',item)
    print(new)