file01 = open(file = 'coffee.txt', mode= 'rt', encoding= 'utf-8')
file02 = open(file = 'coffee_result.txt', mode= 'wt', encoding= 'utf-8')


coffeList = [coffee.strip().split(',') for coffee in file01.readlines()]
discount = dict()
for coffee in coffeList:
    percent = int(coffee[2]) / 100
    discount [coffee[0]] = f'{coffee[2]}% 할인'
    pay = (int(coffee[2]) * int(coffee[1]))
    discountpay = pay - (pay * percent)
    orders = f'{coffee[0]}/{coffee[1]}/{coffee[2]}/{discountpay}\n'
    file02.write(orders)
# end for
print(discount)
file02.close()
with open(file = 'coffee_result.txt', mode= 'rt', encoding= 'utf-8') as file:
    print(file.read())

file01.close()


