"""
Создайте программу создающую папку target внутри которой еще 10 папок имена которых цифры от 1 до 10
"""
import os

os.mkdir(r"/Users/chipolitta/Documents/target")
os.chdir(r"/Users/chipolitta/Documents\target")

for i in range(1, 11):
    os.mkdir(f"{i}")