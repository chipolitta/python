from queue import Queue
from threading import Thread

students = Queue()


def get_students():
    surname = input("Фамилия:")
    for i in range(len(surname)):
        if surname == 'off':
            return 'The end'
        else:
            students.put(surname)


def studentOff():
    print('Вы отчислены:', students.get())


def main():
    get_thread = Thread(target=get_students, args=(students,), daemon=True)
    get_thread.start()
    delete_thread = Thread(target=studentOff, args=(students,), daemon=True)
    delete_thread.start()
    get_thread.join()
    students.join()


print(main())