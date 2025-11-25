try:
    su1 = 10
    su2 = 20

    result = su1 + su2
    print(result)

    mydict = {'hong': 10, 'kim': 20}
    findKey = 'choi'
    print(mydict[findKey])

except TypeError as err:
    print(f'예외 발생 : {err}')
except KeyError as err:
    print(f'예외 발생 : {err}')

else:
    print('예외가 발생하지 않으면 실행됩니다.')

finally:
    print('예외 발생 여부와 상관없이 무조건 실행됩니다.')


