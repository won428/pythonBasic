fruits = ['사과','감','오렌지','한라봉','바나나']

for (idx, value) in enumerate(fruits):
    message = f'{idx + 1}번째 품목은 {value}입니다.'
    print(message)
# end for
print('-'*30)

enum = list(enumerate(fruits))
print(enum)
print('-'*30)

for (idx, value) in enumerate(fruits, start= 1):
    message = f'{idx}번째 품목은 {value}입니다.'
    print(message)
# end for
print('-'*30)

for item in enumerate(fruits, start=1):
    message = f'{item[0]}번째 품목은 {item[1]}입니다.'
    print(message)
# end for
print('-'*30)

print('* 기호는 가변 매개 변수로 인식이 되며, 내부적으로 tuple로 처리됩니다.')
for item in enumerate(fruits):
    # message = '{}번째 값 : {}'.format(item[0], item[1])
    message = '{}번째 값 : {}'.format(*item)
    print(message)