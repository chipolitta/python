def calcluate(*n):
    m = []
    for number in n:
        if number > sum(n) // len(n):
            m.append(number)
            return (sum(n) // len(n), m)


print(calcluate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))