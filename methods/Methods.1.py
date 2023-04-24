from datetime import date

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def ptintname(self):
        print(self.name, self.age)

    @classmethod
    def classmethod(cls, year):
        return Person("polina", date.today().year - year)

    @staticmethod
    def staticmethod(age):
        if age < 18:
            return "no"
        else:
            return "yes"


polina = (Person.classmethod(2004))
print(polina.name)
print(polina.age)
print(polina.staticmethod(18))
