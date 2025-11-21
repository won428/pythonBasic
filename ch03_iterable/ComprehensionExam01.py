mylist01 = [idx for idx in range(1,5)]
print(mylist01)

mylist02 = [idx * 10 for idx in range(1,6)]
print(mylist02)

mylist03 = [idx for idx in range(1,101,3)]
print(mylist03)

mylist04 = [idx for idx in range(1,101,3) if idx%10 == 0]
print(mylist04)

examGrade = [75, 30, 85, 50]  # 합격 기준은 60점 이상

passList = [grade for grade in examGrade if grade >= 60]
print(passList)
print(f'총 {len(passList)}명 합격')

# 다음 항목들을 이용하여 사전으로 만들어 보세요
# 다음은 튜플 요소 3개를 담고 있는 과일 리스트 입니다.
fruits = [('바나나', 10),('사과', 20),('오렌지', 30)]

# dict(사전) comprehension
mydict01 = {key: value for key, value in fruits}
print(mydict01)
print(mydict01['바나나'])

# 학생들의 시험 점수를 사전으로 만들어 보세요.
students = [
    ('이문식', 80, 90, 50),
    ('강수현', 50, 60, 80),
    ('윤정혁', 70, 40, 60)
]
mydict02 = {key : (value, value2, value3) for key, value, value2, value3 in students}
mydictSum02 = {key : sum((value, value2, value3)) for key, value, value2, value3 in students}
# mydict02 = {key[0] : key[1:] for key in students}
# mydictSum02 = {key[0] : sum(key[1:]) for key in students}
print(mydict02)
print(mydictSum02)
