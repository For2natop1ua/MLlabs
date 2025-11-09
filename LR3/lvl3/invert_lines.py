def invert_lines(filename, symbol):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Рядки, що закінчуються на '{symbol}', у перевернутому вигляді:")
    for line in lines:
        line_stripped = line.rstrip()
        if line_stripped.endswith(symbol):
            print(line_stripped[::-1])


invert_lines("rozklad.txt", "к")
