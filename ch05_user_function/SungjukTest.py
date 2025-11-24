def my_avg(name, kor, eng = 60, math = 60):
    avg = (kor + eng + math)/3
    if avg >= 70:
        print(f'{name}님의 평균 점수는 {avg}점 입니다. 합격 입니다.')
    else:
        print(f'{name}님의 평균 점수는 {avg}점 입니다. 불합격 입니다.')
# end def
name, kor, eng, math = '김철수', 50, 60, 70

my_avg(name,kor,eng,math)

my_avg('박영희', 90)

my_avg(math=30,eng=90,name='심현철',kor=100)