def fibonacci(n):
    if n <= 0:
        return "n повинно бути натуральним числом"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


n = 6
print(f"{n}-е число Фібоначчі = {fibonacci(n)}")