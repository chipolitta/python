file_or = input('Введите имя исходного файла')
file_un = input('Введите имя целефого файла')


with open(file_or, 'r') as f, open(file_un, 'w') as d:
    data = f.readlines()
    print(data)
    for i in range(len(data)):
        d.write(f'{i}: {data[i]}')