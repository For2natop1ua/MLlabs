def table(func, values):
    table = {}
    for v in values:
        table[v] = func(v)
    return table


values = [1, 2, 3, 4, 5]
print("Таблиця значень функції x^2:", table(lambda x: x ** 2, values))
