from idlelib.configdialog import changes

coffee = 3
price = 2000
totalPrice = coffee * price

# 기호 {} : format placeholder 또는 format field
message = f'우리 매장에는 커피 {coffee}잔이 판매 가능합니다.'
print(message)

message = '커피 1잔의 가격은 {}원 입니다.'
print(message.format(price))

message = f'커피 {coffee}잔의 가격은 {totalPrice}원 입니다.'
print(message)

message = '커피 {}잔, 단가 : {}원'
print(message.format(coffee, price))

message = f'커피 {coffee}잔, 총금액 : {totalPrice}원'
print(message)

message = '커피 {0}잔, 단가 : {1}원'
print(message.format(coffee, price))

message = '커피 {1}잔, 단가 : {0}원'
print(message.format( price, coffee))

money = 5000
print( '{}원을 입금하였습니다.'.format(money))

change = money - price
message = '거스롬돈 : {}, 판매  : {}잔'
print(message.format(change,1))

coffee = coffee -1
change = money - price
message = '남은 커피는 {}잔 입니다.'
print(message.format(coffee))

