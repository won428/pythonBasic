import somefolder.mymath.MathModule
from somefolder.mymath import MathModule
from somefolder.mymath.MathModule import square_root
from somefolder.mymath.MathModule import jegob # 모든 함수를 가져오고 싶을땐 함수 위치에 *을 넣어서 모든 함수를 가져옵니다.

print(somefolder.mymath.MathModule.square_root(4))
print(MathModule.square_root(4))
print(square_root(4))

print(somefolder.mymath.MathModule.jegob(2,3))
print(MathModule.jegob(2,3))
print(jegob(2,3))

print('# 별칭 사용하기')
import somefolder.mymath.MathModule as imsi
su = 9
result = imsi.square_root(9)
print(f'루트 04 : {result}')
