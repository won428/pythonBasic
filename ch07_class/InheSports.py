class publicInfo:
    def __init__(self, name, entry):
        self.name = name
        self.entry = entry

    def public(self):
        print(f'종목 : {self.name}')
        print(f'엔트리 : {self.entry}명')

class BaseBall(publicInfo):
    def __init__(self, name, entry, hit):
        super().__init__(name, entry)
        self.hit = hit

    def showInfo(self):
        super().public()
        print(f'타율 : {self.hit}')

class FootBall(publicInfo):
    def __init__(self, name, entry, goals):
        super().__init__(name, entry)
        self.goals = goals

    def showInfo(self):
        super().public()
        print(f'골수 : {self.goals}')

base = BaseBall('야구', 9, 0.235)
base.showInfo()
print('-' * 20)
foot = FootBall('축구', 11, 5)
foot.showInfo()
print('-' * 30)
