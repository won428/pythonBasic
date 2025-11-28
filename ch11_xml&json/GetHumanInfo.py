import datetime
import json
from datetime import date
# humans.json 파일을 이용하여 튜플 요소를 담고 있는 list를 생성해 보세요.
# 튜플의 요소는 (이름, 나이, 주소, 취미, 주민 번호, 성별, 혈액형)의 순서대로 명시되어야 합니다.
#
# <class 'str'>
# loads 함수는 문자열을 읽어서 dict 타입으로 변환해 줍니다.
# <class 'list'>
# [('유현식', 12, '공덕동', '독서', '121122-3123456', '남자', 'O형'), ('한지민', 35, '용강동', '영화감상', '891225-2710567', '여자', 'A형')]
filename = 'humans.json'
myfile = open(file= filename, mode= 'rt', encoding= 'utf-8')
mystring = myfile.read()

humans = json.loads(mystring)
print(type(humans))
humanList = list()
for human in humans:
    name = human['name']
    hobby = human['hobby']
    address = human['address']
    blood = human['blood']
    ssn = human['ssn']
    gender = '남자' if ssn[7] in [1,3] else '여자'
    year = int(ssn[0:2])
    today = date.today()
    if year > 50:
        age = 2025 - (1900 + year)
    else:
        age = 2025 - (2000 + year)
    mytuple = (name,f'{age}살' ,hobby, address, f'{blood}형', gender)
    humanList.append(mytuple)

print(humanList)


