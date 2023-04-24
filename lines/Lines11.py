number = '+79918069162'
print('<a href="tel:"' + number + '"' + '>' + number + "</a>")
inp = '<a href="tel:+79918069162">+79918069162</a>'
result = ''
for i in inp:
    if i.isdigit() == True:
        result += i
    else:
        pass
    print(result)