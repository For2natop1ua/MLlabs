def count_file_stats(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)
    print(f"Файл: {filename}")
    print(f"Кількість рядків: {num_lines}")
    print(f"Кількість слів: {num_words}")
    print(f"Кількість символів: {num_chars}")


count_file_stats("rozklad.txt")