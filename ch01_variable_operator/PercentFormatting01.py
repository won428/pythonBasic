name = '김철수'
age = 30
height = 175.3456789
address = '마포'

print('이름 : %s, 나이 : %d' % (name, age))
print('나이 : %d' % (age))
print('키01 : %f' % (height)) # 실수의 기본 값은 소수점 6자리까지 허용
print('키02 : %.2f' % (height))
print('키03 : [%10.3f]' % (height))
print('주소 : %s' % (address) )
message = '이름은 %s이고, 나이는 %d살입니다.'
print(message % (name, age))

su01 = 3
su02 = 5
message = '%d 더하기 %d는 %d입니다.'
print(message % (su01, su02, (su01 + su02)))

a = 2
b = 10
message = '%d의 %d승은 %d입니다.'
print(message % (a, b , pow(a,b)))

hello = '안녕'
message = '[%10s]' %  hello
print(message)

hello = '안녕'
message = '[%-10s]' %  hello
print(message)