x = 5
start = input('Напишите Game, чтобы начать игру:')
while start == 'Game' and x > 0:
    answer = str(input('Угодай число:'))
    if answer == 'Off':
        break
    elif answer == '5':
        print('Вы выйграли билет на концерт!')
    else:
        x -= 1
        if x == 0:
            print('У вас кончились попытки!')
            x = 3
        else:
            print('Попробуйте еще!')
