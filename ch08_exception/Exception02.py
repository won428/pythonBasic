# 품목을 주문하되, 존재하지 않으면 예외 발생시키기

def coffeeCheck(findItem):
    menu = ['아메리카노','라떼','카푸치노','바닐라라떼','모카']
    boolean = findItem in menu
    if boolean:
        print(f'{findItem}을(를) 주문하였습니다')
    else: # 예외 발생 시키기 : raise 사용, 자바의 throw
        message = f'{findItem}은(는) 없는 메뉴입니다.'
        raise Exception(message)

try:
    orderList = ['아메리카노', '핫초코']
    for item in orderList:
        coffeeCheck(item)
except Exception as err:
    print(f'예외 발생 : {err}')