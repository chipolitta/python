class Man():
    def makesound(self):
        print('Имитирует кряканье.')

    def clother(self):
        print('Человек в пальто.')

class Duck():

    def makesound(self):
         print('Кря-кря!')

    def clother(self):
         print('Утка с бантом.')

person = Man()
animal = Duck()

for smth in (person, animal):
        smth.makesound()
        smth.clother()
