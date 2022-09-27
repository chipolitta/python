A = input('Ведите число:')
if int(A[-1]) % 2 == 0 and sum(map(int, A.split())) % 3 == 0:
    print()