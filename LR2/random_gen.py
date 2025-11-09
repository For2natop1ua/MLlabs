import random


def yes_no(condition):
    return "Так" if condition else "Ні"


gene_A_start = 1000
gene_A_end = 3400
gene_B_start = 3700
gene_B_end = 6000
pos = random.randint(1, 6000)
in_gene_A = gene_A_start <= pos <= gene_A_end
in_gene_B = gene_B_start <= pos <= gene_B_end
between_genes = gene_A_end < pos < gene_B_start
in_either_gene = in_gene_A or in_gene_B
outside_genes = not in_either_gene and not between_genes
within_100_to_gene_A_start = (gene_A_start - 100) <= pos < gene_A_start
print(f"Випадкова позиція: {pos}")
print(f"Позиція в гені A? {yes_no(in_gene_A)}")
print(f"Позиція в гені B? {yes_no(in_gene_B)}")
print(f"Позиція між генами A і B? {yes_no(between_genes)}")
print(f"Позиція в одному з генів? {yes_no(in_either_gene)}")
print(f"Позиція поза обома генами? {yes_no(outside_genes)}")
print(f"Позиція в межах 100 до початку гена A? {yes_no(within_100_to_gene_A_start)}")