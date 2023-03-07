import os
import glob
import threading
import time

def replace(filepath):
    with open(filepath, "r") as file:
        content = file.read()
    content = content.replace("ids", "id")
    with open(filepath, "w") as file:
        file.write(content)

def process():
    start_time = time.time()
    files = glob.glob("files/*.txt")
    threads = []
    for file in files:
        thread = threading.Thread(target=replace, args=(file,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Программа выполнена за {end_time - start_time} секунд")

if __name__ == "__main__":
    process()