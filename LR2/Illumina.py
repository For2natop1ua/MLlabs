read = """AATGATACGGCGACCACCGAGATCTACACGCCTCCCTCGCGC
CATCAGAGAGTCTGGGTCTCAGGTACCGCAGTTGTATCTTGCGCGACTATA
ATCCACGGCTCTTATTCTAGCGTGCGCGTACGGCGGTGGGCGTCGTTACGCTATATT"""

nextera_adapter = "AATGATACGGCGACCACCGAGATCTACACGCCTCCCTCGCGCCATCAG"
clean_read = read.replace('\n', '')
read_length = len(clean_read)


def calculate_gc_content(sequence):
    G_count = sequence.count('G')
    C_count = sequence.count('C')
    A_count = sequence.count('A')
    T_count = sequence.count('T')
    total_bases = G_count + C_count + A_count + T_count
    if total_bases == 0:
        return 0.0
    gc_content = (G_count + C_count) / total_bases
    return gc_content * 100


initial_gc = calculate_gc_content(clean_read)
is_adapter_present = nextera_adapter in clean_read
adapter_presence = "Так" if is_adapter_present else "Ні"
adapter_length = len(nextera_adapter)
trimmed_read = clean_read.replace(nextera_adapter, '', 1)
trimmed_gc = calculate_gc_content(trimmed_read)
trimmed_length = len(trimmed_read)
gc_change = trimmed_gc - initial_gc
if gc_change > 0:
    change_status = f"Так, збільшився на {gc_change:.2f}%"
elif gc_change < 0:
    change_status = f"Ні, зменшився на {abs(gc_change):.2f}%"
else:
    change_status = "Ні, залишився незмінним."
print(f"Довжина зчитування: {read_length} нуклеотидів.")
print(f"GC вміст початкового зчитування: {initial_gc:.2f}%")
print(f"Чи присутній адаптер Nextera ({adapter_length} н.т.) у прочитаному? {adapter_presence}")
print(f"Нова довжина зчитування після обрізання: {trimmed_length} нуклеотидів.")
print(f"GC вміст після обрізання: {trimmed_gc:.2f}%")
print(f"Чи збільшився вміст GC після обрізання адаптера? {change_status}")