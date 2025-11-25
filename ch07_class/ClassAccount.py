class Acccount: # 클래스 정의
    bankname = 'KB' # 클래스 변수

    def __init__(self, name, no, deposit):
        # 인스턴스 변수 : self키워드를 사용하여 선언한 변수
        self.name = name
        self.no = no
        self.deposit = deposit

    def printData(self):
        print(f'주거래 은행 : {Acccount.bankname}')
        print(f'예금주 : {self.name}')
        print(f'계좌번호 : {self.no}')
        print(f'예치금 : {self.deposit}')
# end class Account

soo = Acccount('김철수', 1234,1000) # 객체 생성
soo.printData()
print()
hee = Acccount('박영희', 5678,2000) # 객체 생성
hee.printData()