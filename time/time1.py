from time import *


def chess():
    total = 1800
    place = ''
    while place != "off" and total >= 0:
        start = time()
        place = input()
        end = time()
        total = round(total - end + start, 2)
        if total <= 0:
            break
        print(total)

chess()