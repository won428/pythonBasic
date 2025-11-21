# list comprehension을 활용한 문제
# 평균 이상 점수를 받은 학생 수 출력하기
scores = [55, 80, 92, 45, 68, 88]  # 평균 이상이면 '우수'
avg = sum(scores) / len(scores)
avgUp = [score for score in scores if score >= avg ]
print(avgUp)

# 나이가 18세 이상인 사람만 추출하여 몇 명인지 출력
ages = [12, 17, 18, 20, 35, 15]
ageUp = [age for age in ages if age >= 18]
print(len(ageUp))

# 양수만 골라서 개수 출력하기
numbers = [-5, 3, 0, 7, -2, 10, -8]
plusNumbers = [number for number in numbers if number > 0]
print(plusNumbers)

# 짝수만 골라서 출력 및 개수 표시
data = [1, 4, 7, 10, 13, 16]
even = [number for number in data if number%2 == 0]
print(even, len(even))

# 이름 리스트에서 3글자 이상인 이름만 추출
names = ["유나", "철수", "민지", "Tom", "Ann", "Jennifer"]
name3 = [name for name in names if len(name) >= 3]
print(name3)
