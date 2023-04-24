from random import randint

number = int(input('Число участников сборной: '))
cup1 = randint(1, number)
cup2 = randint(1, number)
while cup1 == cup2:
    cup2 = randint(1, number)
print(cup1, '-', cup2)