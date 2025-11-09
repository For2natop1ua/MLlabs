import math

side = float(input("Введіть сторону правильного шестикутника: "))
perimeter = 6 * side
area = (3 * math.sqrt(3) * side**2) / 2

print("Периметр шестикутника =", perimeter)
print("Площа шестикутника =", area)