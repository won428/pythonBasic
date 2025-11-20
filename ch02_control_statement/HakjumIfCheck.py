name = input('이름 : ')
kor = float(input('국어 점수 : '))
eng = float(input('영어 점수 : '))
math = float(input('수학 점수 : '))

total = kor + eng + math
ave = total / 3.0

if ave >= 90 or ave <= 100 :
    hakjum = 'A'
    comment = '최우수 점수 입니다.'
elif ave >= 80 :
    hakjum = 'B'
    comment = '우수 점수 입니다.'
elif ave >= 70 :
    hakjum = 'C'
    comment = '평균 점수 입니다.'
elif ave >= 60 :
    hakjum = 'D'
    comment = '하위 점수 입니다.'
elif ave < 60 :
    hakjum = 'F'
    comment = '최하위 점수 입니다.'
else:
    hakjum = 'null'
    comment = '올바른 점수를 입력해 주세요.'

print(f'{name}님의 정보')
print(f'국어 : {kor}, 영어 : {eng}, 수학 : {math}')
print(f'총점 : {total}\n평균 : {ave}\n학점 : {hakjum}\n코멘트 : {comment}')