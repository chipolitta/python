def name(n):
    let = n[-1]
    if let == 'А' or let == 'Я' or let == 'Г' or let == 'М':
        gen = lambda n, genius: print(n, genius)
        gen(n, 'гений')
    elif let == 'О' or let == 'Ь' or let == 'Л' or let == 'Н':
        gen = lambda n, mind: print(n, mind)
        gen(n, 'сверхразум')
    else:
        gen = lambda  just,n: print(just, n)
        gen('просто', n)
n = input('Whats your name?').swapcase()


name(n)