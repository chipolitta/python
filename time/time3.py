from random import *

a = input()
while True:
    if a == 'off':
        break
    else:
        print('Ваш номер: ', randint(1, 2))
        print('Участников в первом забеге:', randint(2, 50), ',', 'участников во втором забеге:', randint(2, 50))
        a = input()