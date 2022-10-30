with open('file', 'w+') as f:
    f.write('Я гений и стараюсь цчить питон')
    f.seek(0)
    open = f.read(7)
print(open)