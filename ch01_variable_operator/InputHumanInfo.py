# input() 함수는 무조건 문자열(string)로 취급합니다.


print('이름 입력 : ', end= '')
name = input()
age = int(input('나이 입력 : '))
height = float(input('키 입력 : '))

print('\n% 포맷 코드 형식으로 출력')
print('이름 : %s' % name)
print('나이 : %d' % age)
print('키 : %.2f' % height)

print('\nformat() 함수를 사용한 출력')
message = f'제 이름은 {name}이고, 나이는 {age}세 입니다. \n제 키는 {height:.2f}cm입니다.'
print(message)