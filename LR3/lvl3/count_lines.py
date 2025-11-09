def count_lines(filename):
    symbol = input("Введіть символ, на який повинні закінчуватись рядки: ")
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    count = sum(1 for line in lines if line.rstrip().endswith(symbol))
    print(f"Кількість рядків, які закінчуються на '{symbol}': {count}")


count_lines("rozklad.txt")
