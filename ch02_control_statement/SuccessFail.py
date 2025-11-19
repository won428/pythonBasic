midTest = float(input('중간 고사 점수 : '))
finalTest = float(input('기말 고사 점수 : '))
midPercent = 0.4
finalPercent = 0.6
grade = midTest * midPercent + finalTest * finalPercent

if grade >= 70:
    result = '합격'
else:
    result = '불합격'
# end if

message = f'중간 고사 점수 : {midTest:.2f}\n기말 고사 점수 : {finalTest:.2f}\n 점수 : {grade:.2f}\n합격 여부 : {result}'
print(message)