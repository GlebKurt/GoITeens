print("Введіть координати для")
y = int(input("Y: "))
x = int(input("X: "))

def coordinates():
    if y < 0 and x < 0:
        return "1 чверть"
    elif y > 0 and x < 0:
        return "2 чверть"
    elif y > 0 and x > 0:
        return "3 чверть"
    elif y < 0 and x > 0:
        return "4 чверть"
    else:
        "Точка знаходиться на осі"

print(coordinates())