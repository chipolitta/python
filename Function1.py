"""
Напишите программу печатающую бейджики учеников.
Программа запрашивает ввод числа учеников и печатает каждому бейджик. Бейдж содержит название учебного заведения:
«Колледж Сириус», поле для имени:
«Имя: ____» и поле для школы:
«Группа: ____». Напиши программу, печатающую бейджики студентов как на картинке. В завершении программа должна печатать:
«Готово! Заберите бейджики.»
Функция должна принимать имя и группу ученика.
"""

def print_label():
    print('"Колледж Сириус"')
    print('Имя: ____')
    print('Группа: ____')


print('Печать бейджов')
numbers = int(input('Число учеников:'))
for i in range(numbers):
    print_label()
print('Готово! Заберите бейджики.')