class Bank_account():
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport

    def getpassport(self):
        return self.passport

    def getbalance(self):
        return self.balance

    def setPassport(self):
        password = input('Введите пароль:')
        while password != '61218':
            if password == '61218':
                self.passport = 123456

            else:
                print('Попробуйте еще раз!')
                password = input('Введите пароль:')
        print('Данные вашего паспорта изменены. \nНомер вашего паспорта:', self.passport)

    def setBalance(self):
        newBalance = ''
        while self.balance > 0 and newBalance != 0:
            print('Вам доступно:', self.balance)
            newBalance = int(input('Введите сумму, которую хотите снять:'))
            if newBalance <= self.balance:
                self.balance -= newBalance
            else:
                print('У вас недостаточно средств.')
        print('Всего доброго! Хорошего вам дня!')
        return ''


    def delpassport(self):
        password = ''
        while password != '61218':
            password = input('Введите пароль:')
            if password == '61218':
                del self.passport
            else:
                print('Пароль неверный, попробуйте еще раз.')
        print('Ваш паспорт удален.')



chipolitta = Bank_account('', 61218, 123456_123)
print(chipolitta.delpassport())
print(chipolitta.getpassport())
