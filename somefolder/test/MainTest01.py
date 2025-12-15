import somefolder.mymath.MathModule

# import 구문만 사용시 패키지 경로가 길어지면 코드가 좀 길어집니다.
print('# import 구문 사용하기')
su = 4
result = somefolder.mymath.MathModule.square_root(su)
print('루트 01 :', result)

su1 = 2
su2 = 3
result = somefolder.mymath.MathModule.jegob(su1, su2)
print('제곱의 합 01 :', result)

print('# from 패키지경로.모듈이름 import 함수')
# from somefolder.mymath.MathModule import *
from somefolder.mymath.MathModule import square_root
su = 3
result = square_root(su)
print('루트 02 :', result)

from somefolder.mymath.MathModule import jegob
su1 = 3
su2 = 4
result = jegob(su1, su2)
print('제곱의 합 02 :', result)

print('# from 패키지경로 import 모듈이름')
from somefolder.mymath import MathModule
su = 5
result = MathModule.square_root(su)
print('루트 03 :', result)

su1 = 5
su2 = 6
result = MathModule.jegob(su1, su2)
print('제곱의 합 03 :', result)

print('# 별칭 사용하기')
import somefolder.mymath.MathModule as imsi
su = 9
result = imsi.square_root(su)
print('루트 04 :', result)





