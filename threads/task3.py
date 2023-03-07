import threading
import time

def input_():
    while True:
        print("Вводите код быстрее.")
        time.sleep(3)

def main():
    bomb_code = "3141592"
    threading.Thread(target=input_).start()

    while True:
        code = input("Введите код:")
        if code == bomb_code:
            print("Бомба обезврежена.")
        else:
            print("Вы взорвались.")

if __name__ == "__main__":
    main()