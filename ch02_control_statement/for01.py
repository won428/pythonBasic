total01 = 0
for i in range(1,11):
    total01 += i

print(f'총합01 : {total01}')

total02 = 0
for i in range(1, 101, 3):
    total02 += i

print(f'총합02 : {total02}')

total03 = 0
for i in range(97, 1, -5):
    total03 += i

print(total03)

total04 = 0
for i in range(1, 97, 5):
    total04 += pow(i, 2)

print(total04)

total05 = 0
for i in range(1, 6):
    total05 += i * (i+1)

print(total05)