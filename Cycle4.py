review =''
while True:
    review = input('Введите отзыв:').lower()
    if review == ' off':
        print('Сситема предпотений настроена.')
        break
    else:
        print('Спасибо, ваш отзыв принят!')