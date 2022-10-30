with open(input(), 'r') as f:
    d = {}
    for line in f.readlines():
        for word in (''.join(([(lambda x: x if x.isalnum() else '')(x) for x in line])).split()):
            if word in d: d[word] += 1
            else: d[word] = 1
        print(''.join(([k for k, v in d.items() if v == max(d.values())])))