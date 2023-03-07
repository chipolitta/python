
from multiprocessing import Process, Pipe


def money(conn, val):
    conn.send(int(val) * 75)
    conn.close()


if __name__ == '__main__':
    val = input('Введите количество валюты: ')
    while val != 'off':
        first_conn, sin_conn = Pipe()
        p = Process(target=money, args=(sin_conn, val))

        p.start()
        print(first_conn.recv())
        p.join()
        val = input('Введите количество валюты: ')