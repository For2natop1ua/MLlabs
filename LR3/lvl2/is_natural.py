def is_natural(n):
    if n == 1:
        return True
    elif n <= 0:
        return False
    else:
        return is_natural(n - 1)


x = 5
print(f"{x} є натуральним? {is_natural(x)}")
x = 0
print(f"{x} є натуральним? {is_natural(x)}")