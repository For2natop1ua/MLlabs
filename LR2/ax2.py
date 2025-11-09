import math

a = 10
b = 1
x1 = math.sqrt(b / a)
x2 = -math.sqrt(b / a)
check1 = a * x1**2 - b
check2 = a * x2**2 - b

print(f"Нулі рівняння: x1 = {x1}, x2 = {x2}")
print(f"Перевірка для x1: {check1}")
print(f"Перевірка для x2: {check2}")