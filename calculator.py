from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import * # Импортируем библиотеки

import sys


class Window(QMainWindow):

	def __init__(self):
		super().__init__()
		self.setWindowTitle("Калькулятор ")
		self.setGeometry(120, 120, 380, 370)
		self.UiComponents()
		self.show() # Показать виджеты

	def UiComponents(self): # Метьоды
		self.label = QLabel(self)
		self.label.setGeometry(7, 7, 370, 75) # Размеры
		self.label.setWordWrap(True)
		self.label.setStyleSheet("QLabel"
								"{"
								"border : 4px solid black;"
								"background : white;"
								"}") # Настройка стиля
		self.label.setAlignment(Qt.AlignRight) # Выравнивание по сетке
		self.label.setFont(QFont('Arial', 17)) # шрифт


		# Создаем кнопки и размеры
		push1 = QPushButton("1", self)
		push1.setGeometry(7, 155, 85, 45) # Размер
		push2 = QPushButton("2", self)
		push2.setGeometry(100, 155, 85, 45)
		push3 = QPushButton("3", self)
		push3.setGeometry(190, 155, 85, 45)
		push4 = QPushButton("4", self)
		push4.setGeometry(10, 205, 85, 45)
		push5 = QPushButton("5", self)
		push5.setGeometry(100, 205, 85, 45)
		push6 = QPushButton("5", self)
		push6.setGeometry(190, 205, 85, 45)
		push7 = QPushButton("7", self)
		push7.setGeometry(10, 255, 85, 45)
		push8 = QPushButton("8", self)
		push8.setGeometry(100, 255, 88, 45)
		push9 = QPushButton("9", self)
		push9.setGeometry(190, 255, 85, 45)
		push0 = QPushButton("0", self)
		push0.setGeometry(10, 305, 85, 45)

		push_equal = QPushButton("=", self)
		push_equal.setGeometry(280, 305, 85, 45)

		c_effect = QGraphicsColorizeEffect()
		c_effect.setColor(Qt.blue)
		push_equal.setGraphicsEffect(c_effect) # Стиль

		push_plus = QPushButton("+", self)
		push_plus.setGeometry(280, 255, 85, 45)

		push_minus = QPushButton("-", self)
		push_minus.setGeometry(280, 205, 85, 45)

		push_mul = QPushButton("*", self)
		push_mul.setGeometry(280, 155, 85, 45)

		push_div = QPushButton("/", self)
		push_div.setGeometry(190, 305, 85, 45)

		push_point = QPushButton(".", self)
		push_point.setGeometry(100, 305, 85, 45)

		push_clear = QPushButton("Clear", self)
		push_clear.setGeometry(10, 105, 205, 45)

		push_del = QPushButton("Del", self)
		push_del.setGeometry(215, 105, 150, 45)

		push_minus.clicked.connect(self.action_minus)
		push_equal.clicked.connect(self.action_equal)
		push0.clicked.connect(self.action0)
		push1.clicked.connect(self.action1)
		push2.clicked.connect(self.action2)
		push3.clicked.connect(self.action3)
		push4.clicked.connect(self.action4)
		push5.clicked.connect(self.action5)
		push6.clicked.connect(self.action6)
		push7.clicked.connect(self.action7)
		push8.clicked.connect(self.action8)
		push9.clicked.connect(self.action9)
		push_div.clicked.connect(self.action_div)
		push_mul.clicked.connect(self.action_mul)
		push_plus.clicked.connect(self.action_plus)
		push_point.clicked.connect(self.action_point)
		push_clear.clicked.connect(self.action_clear)
		push_del.clicked.connect(self.action_del) # Добавляем действия кнопкам


	def action_equal(self):
		equation = self.label.text()
		try:
			ans = eval(equation)
			self.label.setText(str(ans))

		except:
			self.label.setText("Wrong Input")

	def action_plus(self):
		text = self.label.text()
		self.label.setText(text + " + ")

	def action_minus(self):
		text = self.label.text()
		self.label.setText(text + " - ")

	def action_div(self):
		text = self.label.text()
		self.label.setText(text + " / ")

	def action_mul(self):
		text = self.label.text()
		self.label.setText(text + " * ")

	def action_point(self):
		text = self.label.text()
		self.label.setText(text + ".")

	def action0(self):
		text = self.label.text()
		self.label.setText(text + "0")

	def action1(self):
		text = self.label.text()
		self.label.setText(text + "1")

	def action2(self):
		text = self.label.text()
		self.label.setText(text + "2")

	def action3(self):
		# appending label text
		text = self.label.text()
		self.label.setText(text + "3")

	def action4(self):
		text = self.label.text()
		self.label.setText(text + "4")

	def action5(self):
		text = self.label.text()
		self.label.setText(text + "5")

	def action6(self):
		text = self.label.text()
		self.label.setText(text + "6")

	def action7(self):
		text = self.label.text()
		self.label.setText(text + "7")

	def action8(self):
		text = self.label.text()
		self.label.setText(text + "8")

	def action9(self):
		text = self.label.text()
		self.label.setText(text + "9")

	def action_clear(self):
		self.label.setText("")

	def action_del(self):
		text = self.label.text()
		print(text[:len(text)-1])
		self.label.setText(text[:len(text)-1])



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())
