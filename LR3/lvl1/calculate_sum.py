def calculate_sum(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            print(f"'{num}' не є числом")
    return total


print("Сума чисел:", calculate_sum(1, 2, 3, 'a', 4.5))
