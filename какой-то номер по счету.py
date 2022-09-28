string = 'Экономический рост тесно связан с ростом общего благосостояния.'
A = 'ический'
B = 'ическая'
if A in string:
    string = string.replace(A, '.')
else:
    string = string.replace(B, '.')
print(string)