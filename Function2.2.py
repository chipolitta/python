"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""

def taxi():
    price = 4
    skolko_edem = int(input('Длинна поезди в метрах - '))
    while skolko_edem >= 0:
        if skolko_edem > 140:
            price += 0.25
            skolko_edem -= 140
        elif skolko_edem in range(0, 141):
            price += 0.25
            skolko_edem -= 140
        print(price)


taxi()