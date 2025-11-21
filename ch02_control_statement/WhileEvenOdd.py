odd, even = 0, 0
i =  1
while i < 11:
    if i % 2 == 0:
        even += i
    else:
        odd += i
    # end if
    i += 1
# end while
print(f'홀수의 총합 : {odd}\n짝수의 총합 : {even}')