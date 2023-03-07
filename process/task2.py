
from multiprocessing import Process

file_name = "price.txt"


def write():
    global file_name
    length = 6
    width = 6
    height = 4
    result = (length * height * 2) + (width * height * 2)
    with open(f"{file_name}", "w+") as f:
        f.write(str(result) + "\n")
        pass


def read():
    global file_name
    with open(f"{file_name}", "r") as f:
        x = f.read()
    with open(f"{file_name}", "a+") as file:
        file.write(f"Количество краски для данной комнаты {int(x) * 5}")


if __name__ == "__main__":
    p1 = Process(target=write)
    p2 = Process(target=read)
    p1.start()
    p1.join()
    p2.start()