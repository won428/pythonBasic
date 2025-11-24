# 이름과 나이를 입력 받아서 출력해 줍니다.
def namePrint():
    name = input('이름 입력 : ')
    age = input('나이 입력 : ')
    print(f'이름 : {name}, 나이 : {age}')

#  인사말과 반복 회수 n을 이용하여 인사말을 n번 출력해주는 함수입니다.
def sayHello(message, number = 10):
    for i in range(number):
        print(message)