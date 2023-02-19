"""напишите программу-вирус которая переименовывает папки c четными номерами в ранее созданной папке target,
новые имена придумайте самостоятельно.
"""
import os

list1 = (os.listdir(r"/Users/chipolitta/Documents/target"))

for i in list1:
    if int(i) % 2 == 0:
        os.rename(fr"/Users/chipolitta/Documents/target\{i}",
                  fr"/Users/chipolitta/Documents/target/file2{i}")
