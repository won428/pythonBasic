def nameAgePrint():
    name = input('이름 입력 : ')
    age = int(input('나이 입력 : '))

    print('이름 : %s, 나이 : %d세' % (name, age))
# end def nameAgePrint

def sayHello(message, n = 10):
    for idx in range(n):
        print(message)
    print()
# end def