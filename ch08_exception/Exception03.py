class LessThan5Exception(Exception): # Exception을 상속 받음
    # 입력된 숫자가 5미만일 때 발생시키고자 하는 사용자 정의 예외
    def __init__(self, value):
        self.message = f'{value}는 5보다 작은 수 입니다. 5 이상을 입력해 주셔야합니다.'
        super().__init__(self.message)

    def __str__(self): # 자바의 toString() 개념과 거의 흡사
        return f'LessThan5Exception 클래스 : {self.message}'


su = input('5 이상의 정수를 입력해주세요.')

try:
    su = int(su)
    if su < 5:
        raise LessThan5Exception(su)
    else:
        print(f'{su}가 입력되었습니다.')
except ValueError as err:
    print('올바른 숫자 형식을 입력해 주셔야 합니다.')
    print(err)
except LessThan5Exception as err:
    print(err)
except Exception as err:
    print(f'기타 나머지 예외 발생 : {err}')