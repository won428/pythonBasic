# MathTest01.py
import math

print('math.pi :', math.pi)
print('math.e :', math.e)
print('math.pow(2, 10) :', math.pow(2, 10))
print('math.factorial(5) :', math.factorial(5))
print('math.trunc(123.456789) :', math.trunc(123.456789))
print('math.floor(123.456789) :', math.floor(123.456789))
print('math.ceil(123.456789) :', math.ceil(123.456789))
print('math.sqrt(16) :', math.sqrt(16))
print('math.log(4, 2) :', math.log(32, 2))
print('math.log10(100) :', math.log10(1000))

# 삼각 함수
# 원주율 3.14를 각도로 표현하면 180도입니다.
print('math.degrees(math.pi) :', math.degrees(math.pi))
print('math.radians(180) :', math.radians(180))

print('math.sin(math.pi) :', math.sin(math.pi/2))
print('math.cos(math.pi/2) :', math.cos(math.pi/2))
print('math.tan(math.pi/4) :', math.tan(math.pi/4))

# 각도를 입력하여 라디안으로 변경해주는 함수 deg2rad()를 구현해 보세요.
def deg2rad(degree):
    return math.radians(degree)

degree = int(input('각도 입력 : '))
result = deg2rad(degree)
print('각도 : %d, 라디안 : %f' % (degree, result))

# 다음 list 내의 각 요소인 tuple은 직각 삼각형의 두변에 대한 정보입니다.
# 이를 사용하여 가장 긴 변의 길이를 구하여 새로운 list를 만들어 보세요.
mydata = [(3, 4), (5, 12), (7, 24)]

triangle = []
for item in mydata:
    diag = math.sqrt(math.pow(item[0], 2) + item[1]**2)

    triangle.append((item + (diag,)))
# end for

print(triangle)

# softmax 함수는 머신 러닝에서 다중 분류를 처리하기 위한 알고리즘 중의 하나입니다.
def softmax(mylist):
    newlist = [math.exp(val) for val in mylist]
    total = sum(newlist)

    for idx in range(len(newlist)):
        newlist[idx] /= total

    return newlist
# end def


mylist = [0.1, 1.0, 2.0]
result = softmax(mylist)
print(result)