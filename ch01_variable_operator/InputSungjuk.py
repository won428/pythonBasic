name = input('이름 입력 : ')
korGrade = float(input('국어 점수 : '))
engGrade = float(input('영어 점수 : '))
mathGrade = float(input('수학 점수 : '))
totalGrade = korGrade + engGrade + mathGrade
ave = totalGrade / 3

message = (f'이름 : {name}\n'
           f'국어 입력 : {korGrade}\n'
           f'영어 입력 : {engGrade}\n'
           f'수학 입력 : {mathGrade}\n'
           f'국어 점수 : {korGrade:.2f}\n'
           f'영어 점수 : {engGrade:.2f}\n'
           f'수학 점수 : {mathGrade:.2f}\n'
           f'총점 : {totalGrade:.2f}\n'
           f'평균 : {ave:.2f}')
print(message)