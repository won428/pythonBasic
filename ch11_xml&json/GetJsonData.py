import json
from xml.etree.ElementTree import parse

filename = 'jumsu.json'
myfile = open(file = filename, mode = 'rt', encoding= 'utf-8')
mystring = myfile.read()
myfile.close()

print('loads 함수는 문자열을 읽어서 dict를 원소로 담고 있는 list를 반환해 줍니다.')
jsonData = json.loads(mystring)

# 학생들의 정보를 tuple 형식으로 저장할 list 자료형
studentList = list()
for item in jsonData:
    name = item['name']
    kor = float(item['kor'])
    eng = float(item['eng'])
    math = float(item['math'])
    gender = '남자' if item['gender'].upper() == 'M' else '여자'
    total = kor + eng + math
    if 'hello' in item.keys():
        hello = item['hello']
        newTuple = (name, kor, eng, total, hello, gender)
    else:
        newTuple = (name, kor, eng, total, gender)
    studentList.append(newTuple)
print(studentList)



