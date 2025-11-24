su01 = 14
su02 = 5
# 함수의 정의
# def : define(정의하다)의 줄임말
# 매개 변수 : parameter, argument, 인자, 인수라고 부르기도 합니다.
# 자바와는 달리 매개 변수에 기본값을 할당 할 수 있습니다.
# 오버로딩 개념이 없다고 볼 수 있습니다.
def add(a ,b = 15):
    return a+b
# end def

# positional argument : index를 이용하여 매개 변수에 할당하는 방식
result = add(su01,su02)
print(f'{su01} + {su02} = {result}')
print(f'{100} + {200} = {add(100,200)}')

# keyword argument = 매개 변수 키워드를 이용하여 매개 변수를 할당하는 방식
result = add(a = su02, b = su01)
print(result)

# 혼합 방식
result = add(15, b =20)
print(result)

# 기본 값 이용
def add2(a = 10, *, b):
    return a + b
result = add2(b = 10)
print(result)

