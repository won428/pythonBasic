# Has A 관계 : A 클래스에서, B 클래스를 이용해 만든 객체를 A 클래스가 가지고 있는 관계를 말합니다.
class Bag:
    isOpened = False # 도시릭 가방 열림 여부(기본값 닫힘)

    def open(self):
        print('도시락 가방을 엽니다.')
        self.isOpened = True

    def close(self):
        print('도시락 가방을 닫습니다.')
        self.isOpened = False

    dosirakList = [] # 담기는 도시락들을 저장할 리스트
    def put(self, dosirak):
        if self.isOpened:
            print('# 가방에 도시락을 담았습니다.')
            self.dosirakList.append(dosirak)
        else:
            print('# 도시락 가방이 닫혀 있어, 도시락을 가방에 담을 수 없습니다.')

    def showList(self):
        print('# 도시락 목록 확인')
        for item in self.dosirakList:
            print(f'이름 : {item.name}, 단가 : {item.price}원')
            print(f'반찬 목록 : {item.subList}')



# 도시락 클래스는 가방 클래스의 포함 대상
class Dosirak:
    # 반찬 갯수는 가변적이어서 * 기호를 붙입니다.
    # *은 파이썬에서 내부적으로 tuple로 인식을 합니다.
    def __init__(self, name, price, *subList ):
        self.name = name
        self.price = price
        self.subList = subList

    def info(self):
        print(f'도시락명 : {self.name}')
        print(f'가격 : {self.price}')
        print(f'반찬 : {self.subList}')

mybag = Bag()

dosirak01 = Dosirak('진달래 도시락', 7000, '계란 후라이', '김', '마른 멸치')
mybag.open()
mybag.put(dosirak01)
mybag.close()
print()
dosirak02 = Dosirak('매화 도시락', 10000, '고급 어묵', '김치', '마른 멸치', '단호박 샐러드')
mybag.open()
mybag.put(dosirak02)
mybag.close()
print()
mybag.showList()