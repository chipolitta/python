def way(km):
    if km // 140 <= 1:
        return 4.25
    elif km % 140 > 0:
        return 4 + 0.25 * (km // 140) + 0.25


print(way(141), '$')