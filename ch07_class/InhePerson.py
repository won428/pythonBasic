class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def getName(self):
        return self.name
    def publicInfo(self):
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'성별 : {self.gender}')
#
class Employee(Person): # 서브클래스(슈퍼클래스)
    def __init__(self, name, age, gender, salary, date):
        super().__init__(name, age, gender)
        self.salary = salary
        self.date = date
    def employeeInfo(self):
        super().publicInfo()
        print(f'급여 : {self.salary}')
        print(f'입사일자 : {self.date}')

    def message(self):
        print(f'{super().getName()}님 오늘도 행복하세요.')
#
class Student(Person):
    def __init__(self, name, age, gender, subject, grade):
        super().__init__(name,age,gender)
        self.subject = subject
        self.grade = grade

    def studentInfo(self):
        super().publicInfo()
        print(f'과목 : {self.subject}')
        print(f'학점 : {self.grade}')
#

soo = Employee('김철수', 20, '남자', 50000, '2020/12/25')
soo.employeeInfo()
soo.message()
print()

hee = Student('박영희',19,'여자','국어','A')
hee.studentInfo()

# Person 클래스를 상속 받는 Teacher 클래스를 구현해 보세요.
# kim = Teacher('김유신', 40, '남자', '파이썬')
# kim.showData()
# kim.doTeach() # 파이썬을 가르칩니다.