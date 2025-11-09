def reverse_sequence():
    num = int(input("Введіть число (0 для завершення): "))
    if num == 0:
        return []
    else:
        rest = reverse_sequence()
        return rest + [num]


print("Зворотний порядок:", reverse_sequence())