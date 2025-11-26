coffees = ['아메리카노','카페라떼','카푸치노','바닐라라떼','모카']
file01 = open(file= 'coffee_menu.txt', mode= 'wt', encoding='utf-8')

for idx, coffee in enumerate(coffees):
    if idx % 2 == 0:
        file01.write(f'오늘 추천 커피는 {coffee}입니다. {idx + 1}번째 커피 풍미가 깊어요\n')
    else:
        file01.write(f'오늘 추천 커피는 {coffee}입니다. {idx + 1}번째 커피 부드럽게 즐기세요\n')


for idx, coffee in enumerate(coffees):
    filename = f'{coffee}' + str(idx).zfill(2) + '.txt'
    with open(file= filename, mode= 'wt', encoding= 'utf-8') as coffeeFile:
        message = f'{coffee}를 위한 정보 파일입니다.'
        coffeeFile.write(message)
