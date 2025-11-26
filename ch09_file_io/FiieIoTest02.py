
encoding = 'utf-8'
filename = 'coffee_list.txt'
coffeeList = ['아메리카노', '라떼', '카푸치노', '바닐라라떼', '모카']
with open(file= filename, mode='wt', encoding= encoding) as txt:
    for coffee in coffeeList:
            txt.write(f'{coffee}\n')
    # end for
# end with

file01 = open(file= filename, mode='rt', encoding= encoding)
while True:
    oneline = file01.readline().strip()
    print(oneline)
    if not oneline:
        break
    # end if
# end while
file01.close()

file02 = open(file= filename, mode='rt', encoding= encoding)
coffees = file02.readlines()
for coffee in coffees:
    print(coffee.strip())
# end for
file02.close()
print()

file03 = open(file= filename, mode='rt', encoding= encoding)
print(file03.read())
file03.close()