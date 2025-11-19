name = '김철수'
fruit = '사과'
gaesu = 8
su01 = 4
su02 = 9
su03 = -5
a = 2.0
b = 3.0
rate = 0.4567

message = '%s가 %s를 %d개 먹었습니다.' % (name, fruit, gaesu)
print(message)

message = '%d 곱하기 %d는 %d 입니다.' % (su01 , su02, (su01 * su02))
print(message)

message = '%f의 %f제곱은 %f입니다.' % (a, b , pow(a, b))
print(message)

message = '%을 표현하려면 %%를 표시해야합니다.'
print(message)

message = '비율 : %f%%' % (rate * 100)
print(message)

message = '%d의 절댓값은 %d 입니다.' % (su03, abs(su03))
print(message)