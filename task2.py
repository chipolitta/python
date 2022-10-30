with open('dop', 'w+') as f, open('file', 'r') as j:
    lines = j.readlines()
    f.write('\n'.join(lines))
    f.write('... но у меня не получается')
    f.seek(0)
    r = f.read()
    print(r)