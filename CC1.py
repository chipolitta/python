meal = input('Прием пищи:')
meal = meal.lower()
if meal == 'Завтрак':
    print('Каша')
else:
    wish = input('Предпочтение:')
    wish = wish.lower()
    if wish == 'Поесть плотно':
        print('Плов')
    else:
        print('Котлета с пюре')
