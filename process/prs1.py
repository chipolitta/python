import multiprocessing

def chet(start, end):
    result = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            result += i
    return result

def ne(start, end):
    result = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            result += i
    return result

if __name__ == '__main__':
    start = 1
    end = 1000000

    p1 = multiprocessing.Process(target=chet, args=(start, end))
    p2 = multiprocessing.Process(target=ne, args=(start, end))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Сумма четных:", p1.result())
    print("Сумма нечетных:", p2.result())