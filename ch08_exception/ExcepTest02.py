
def checkFunc(check):
    students = ['철수', '영희', '민수', '지영']
    boolean = check in students
    if boolean:
        print(f'{check}은 출석입니다.')
    else:
        message = f'{check}은 결석입니다.'
        raise Exception(message)

try:
    checkList = ['철수', '훈식']
    for check in checkList:
        checkFunc(check)
except Exception as err:
    print(err)
