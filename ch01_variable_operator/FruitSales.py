applePrice = 1000
gamPrice = 500
appleCount = 3
gamCount = 10
money = 10000
payMoney = gamCount*gamPrice + appleCount * applePrice
change = money - payMoney

message = (f'사과 {appleCount}개 구매, 가격 : {applePrice * appleCount}\n'
           f'감 {gamCount}개 구매, 가격 : {gamPrice * gamCount}\n'
           f'내신 금액 : {payMoney}\n'
           f'잔돈 : {change}')
print(message)