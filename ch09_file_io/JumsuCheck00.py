studentList = ['제시카','홍길동','유재석','티파니']
jumsuFilename = 'jumsu02.txt'
resultFileName = 'result02.txt'
encoding = 'utf-8'

with open(jumsuFilename, mode='w', encoding= encoding) as f:
    pass

with open(resultFileName, mode='w', encoding= encoding) as f:
    pass

class studentClass:
    def __init__(self, name, kor, eng, math, gender):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.gender = gender
    # end def
    def addTxt(self):
        with open(file= jumsuFilename, mode = 'at', encoding= encoding) as jumsu:
            jumsu.write(f'{self.name},{self.kor},{self.eng},{self.math},{self.gender}\n')
    # end def
    def addResult(self):
        total = self.kor + self.eng + self.eng
        avg = total/3
        genderStr = '남자' if self.gender == 'M' else '여자'
        with open(file= resultFileName, mode= 'at', encoding= encoding) as result:
            result.write(f'{self.name}/{genderStr}/{total}/{avg:.2f}\n')
    # end def
# end class

for student in studentList:
    print(f'{student}님의 점수를 입력해주세요')
    kor = float(input('국어 : '))
    eng = float(input('영어 : '))
    math = float(input('수학 : '))
    gender = input('성별 (M 또는 F): ')
    if not gender == 'M' and not gender == 'F':
        print('올바른 성별을 입력해주세요')
        break
    # end if
    student01 = studentClass(student, kor, eng, math, gender)
    student01.addTxt()
    student01.addResult()

    with open(file= resultFileName, mode= 'rt', encoding= encoding) as result:
        sentences = result.read()
        print(sentences)
    # end with
# end for

