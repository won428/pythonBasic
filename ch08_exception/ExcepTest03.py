# MinJumsuException : 과락(과목이 40미만), FailedException : 평균 60미만
class MinJumsuException(Exception):
    def __init__(self, name):
        self.message = f'{name}님 과락입니다. '
        super().__init__(self.message)

    def __str__(self):
        return self.message

class FailedException(Exception):
    def __init__(self, name):
        self.message = f'{name}님 불합격입니다.'
        super().__init__(self.message)

    def __str__(self):
        return self.message

class students:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

def PassOrNone(person):
    grades = [person.kor, person.eng, person.math]
    total = person.kor + person.eng +person.math
    avg = total / len(grades)
    for grade in grades:
        if grade < 40:
            raise MinJumsuException(person.name)
        else:
            pass
    if avg < 60:
        raise FailedException(person.name)
    else:
        print(f'{person.name}님 합격입니다.')

studentList = ['김철수','박영희','최민식']
for student in studentList:
    print(f'{student}님의 점수를 입력해주세요')
    name = student
    kor = int(input('국어 : '))
    eng = int(input('영어 : '))
    math = int(input('수학 : '))
    person = students(name, kor, eng, math)
    try:
        PassOrNone(person)
    except MinJumsuException as err:
        print(err)
    except FailedException as err:
        print(err)


# 이름 입력 : 김철수
# 국어 점수 입력 : 50
# 영어 점수 입력 : 60
# 수학 점수 입력 : 90
# 김철수님 합격입니다.
#
# 이름 입력 : 박영희
# 국어 점수 입력 : 100
# 영어 점수 입력 : 100
# 수학 점수 입력 : 20
# 시험을 잘못 보셨군요.
# 박영희님 과락입니다.
#
# 이름 입력 : 최민식
# 국어 점수 입력 : 50
# 영어 점수 입력 : 55
# 수학 점수 입력 : 60
# 조금만 더 공부하시길 바랍니다.
# 최민식님 불합격입니다.