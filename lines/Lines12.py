text = '<spam>58nbsp;1288nbsp;Pc/spam>'
result = ''
for i in text:
    if i.isdigit():
        result += i
        print(result)