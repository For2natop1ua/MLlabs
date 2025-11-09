primer = "TTAGCACACGTGAGCCAATGGAGCAAACGGGTAATT"
GC = primer.count("G") + primer.count("C")
N = len(primer)
Tm = 64.9 + 41 * (GC - 16.4) / N

print("Загальна кількість G і C =", GC)
print("Довжина =", N)
print("Tm =", round(Tm, 2), "°C")
