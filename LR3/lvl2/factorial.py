def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("Факторіал:")
num = 5
print(f"{num}! = {factorial(num)}")