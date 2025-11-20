name = input('이름 : ')
month = int(input('월급 : '))

if month >= 500 :
    year = month * 12
else:
    year = month * 13
# end if
if 0 <= year < 1000:
    tax = 0
elif 1000 <= year < 5000 :
    tax = 0.1
elif 5000 <= year < 10000 :
    tax = 0.15
else:
    tax = 0.2
# end if

myTax = year * tax

print(f'이름 : {name}\n월급 : {month}\n연봉 : {year:.2f}\n세금 : {myTax:.2f}')

