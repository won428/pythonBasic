# 어떤 정수를 0으로 나누려고 하면 예외가 발생합니다.
# 이에 대한 예외 처리를 수행해 보세요.
# 또한, 리스트 목록의 범위를 벗어 나는 요소의 값을 참조하고자 할 때 발생하는 예외에 대한 처리를 수행해 보세요

try:
    x, y = 4, 2

    z = x / y
    print(z)

    mylist = [1,2,3]
#    print(mylist[5])

    dict_fruit = {'사과':10, '바나나':20}
    print(dict_fruit['오렌지'])

    print('예외가 발생하면 이 부분은 실행되지 않습니다.')

except ZeroDivisionError as err: # 0 나누기 에러
    print('0으로 나눌 수 없습니다.')
    print('예외 객체 정보 : %s' % err)

except IndexError as err: # 리스트 밖으로 범위 벗어남
    print('인덱스의 접근 범위를 벗어남')
    print('예외 객체 정보 : %s' % err)

except KeyError as err: # dict에 없는 키를 요청함
    print('dict에 존재하지 않는 Key를 요청함')
    print('예외 객체 정보 : %s' % err)

except Exception as err: # 기타 나머지 에러
    print('기타 나머지 예외 발생')
    print('예외 객체 정보 : %s' % err)

else:
    print('예외가 발생하지 않으면 실행됩니다.')

finally:
    print('예외 발생 여부와 상관없이 무조건 실행됩니다.')
#end try