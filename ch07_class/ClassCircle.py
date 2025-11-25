class Circle:
    shape = 'circle'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def showinfo(self):
        print(f'원 중심 : {self.a}, {self.b}')
        print(f'반지름 : {self.c}')
        print(f'면적 : {self.c * self.c * 3.14}')

print(f'타입 : {Circle.shape}')

circle1 = Circle(3, 5, 10)
circle1.showinfo()
print( '-' * 20 )
circle2 = Circle(8, 6, 20)
circle2.showinfo()