exon_start = 12030
exon_end = 12174

snp1 = 12111
snp2 = 12188

snp1_result = "Так" if (exon_start <= snp1 <= exon_end) else "Ні"
snp2_result = "Так" if (exon_start <= snp2 <= exon_end) else "Ні"

print("\nПеревірка SNP у межах екзону:")
print(f"SNP1 ({snp1}) всередині екзону? {snp1_result}")
print(f"SNP2 ({snp2}) всередині екзону? {snp2_result}")