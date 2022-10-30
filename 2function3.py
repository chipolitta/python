def summa (n = '', result = 0.0):
    n = input()
    if n == '':
        return result
    else:
        result += int(n)
        return summa(int(n), result)


print(summa())