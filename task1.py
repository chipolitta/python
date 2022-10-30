while True:
    a = input('Введите имя:')
    if a != 'off':
        gen = lambda a_, genius: print(a_, genius)
        gen(a, 'гений')
    else:
        break