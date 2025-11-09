def create_a_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(1, 10):
            f.write('a' * i + '\n')
    print(f"Файл '{filename}' створено.")


create_a_file("letters.txt")
