login = input()
forb_sys = '=?*^$№@'
count = 0
for i in login:
    if i in forb_sys:
        print('Недопустимый символ!', i)
        break
    else:
        count +=1
        if count == len(login):
            print('Все хорошо!')
            break