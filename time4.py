from time import sleep

fine = int(input('Удалить с поля? (2 или 10 минут) '))
print('Вы удалены с поля на ', fine, 'минут(-ы).')
if fine == 2:
    sleep(2)
    print('Возвращайтесь на поле!')
elif fine == 10:
    sleep(10)
    print('Возвращайтесь на поле!')