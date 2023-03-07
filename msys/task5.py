import sys

filename = sys.argv[1]

with open(filename) as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith('#'):
            continue

        try:
            exec(line)
        except Exception as e:
            print("Ошибка.")