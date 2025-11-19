name = input('이름 : ')
age = int(input('나이 : '))
_gender = int(input('성별 입력(숫자 1, 2, 3, 4 중 택일) : '))

#start if
if age > 19 :
    adult = '성인'
else:
    adult = '미성년자'
# end if

# start if
if _gender == 1 or _gender == 3:
    gender = '남자'
elif _gender == 2 or _gender == 4:
    gender = '여자'
else:
    gender = '잘못된 입력입니다.'
# end if

message = f'이름 : {name}\n나이 : {age}\n성인 여부 : {adult}\n성별 : {gender}'
print(message)