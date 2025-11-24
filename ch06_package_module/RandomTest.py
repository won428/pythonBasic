import random

print(random.random())

# random.seed(1234) 이처럼 시드를 배정하면 항상 동일한 값이 나옵니다.
print(random.random())

print(random.randint(1,10))

coffees = ['아메리카노','카페라떼','아이스커피','디카페인커피','바닐라라떼']

print(random.choice(coffees))

random.shuffle(coffees)

print(coffees)

lottoNumber = [number for number in range(1, 46)]
random.shuffle(lottoNumber)
print(lottoNumber)

lotto = lottoNumber[0:6]
print(f'당첨 번호 : {lotto}')

def extarctLottoNo(i):
    for idx in range(i):
        random.shuffle(lottoNumber)
        lotto = sorted(lottoNumber[0:6])
        print(f'구매 번호 : {lotto}')

# 5 게임 출력하기
count = 1
extarctLottoNo(count)

# 다음 명단을 이용하여, 1조당 2명씩 조 배정을 해보세요.
MEMBER_SU = 2 # 조원 멤버 수

members = ['이민정', '최현미', '강유식', '김정식', '안미주', '심현철', '오지훈', '이한나']

random.shuffle(members)

for idx in range(0, len(members), MEMBER_SU):
    print(members[idx:idx+MEMBER_SU])

n = 3
sampling = random.sample(members, n)
print(sampling)