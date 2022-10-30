grades = [{'name': 'Jennifer', 'final': 95},
          {'name': 'David', 'final': 92},
          {'name': 'Aaron', 'final': 98}]


a = sorted(grades, key = lambda x: (x['name']))
print(*a)