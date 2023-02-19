""" напишите программу которая создает папку task4 и записывает текст "я выполнил задание" в файл answer.txt
"""
import os

os.mkdir(r"/Users/chipolitta/Documents/task4")
os.chdir(r"/Users/chipolitta/Documents/task4")
text_file = open("answer.txt", "w")
text_file.write("Я выполнила задание")



