import random
from queue import Queue
from concurrent.futures import ThreadPoolExecutor


def numbers(queue, number):
    for i in range(1, number + 1):
        num = random.randint(1, 100)
        queue.put(num)


def division(queue):
    while not queue.empty():
        num = queue.get()
        list = []
        for i in range(1, num + 1):
            if num % i == 0:
                list.append(i)
        print(f"{list} - делители числа {num}")


def main():
    with ThreadPoolExecutor() as Th:
        Th.submit(numbers, queue, number)
        Th.submit(division, queue)
        Th.submit(division, queue)


queue = Queue()
number = int(input("Введите количество чисел: "))

main()
