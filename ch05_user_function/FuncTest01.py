def func01(a, b = 5):
    return (2 * a)+(3 * b)
# end def

su01 = 3
su02 = 5
result = func01(su01,su02)
print(f'(2 * {su01}) + (3 * {su02}) = {result}')
print(f'{func01(10)}')