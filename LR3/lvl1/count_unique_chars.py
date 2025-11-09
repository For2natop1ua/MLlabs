def count_unique_chars(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    unique_count = len(char_counts)

    return unique_count, char_counts


test_string = "Hello World"
unique_count, counts_dict = count_unique_chars(test_string)
print(f"Рядок: '{test_string}'")
print(f"Кількість унікальних символів: {unique_count}")
print(f"Детальний підрахунок: {counts_dict}")
