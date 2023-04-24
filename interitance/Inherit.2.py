class Genius:

    def __init__(self, name):
        self.name = name

    def write_genius(self):
        return f'{self.name} гений!'


class OOP(Genius):

    def __init__(self, name):
        super().__init__(name)

    def make_object(self):
        one = Genius(self.name)
        return one

    def complete(self):
        print(f'{self.make_object().write_genius()}')


def check():
    test = OOP('Маргарита')
    test.complete()


check()
