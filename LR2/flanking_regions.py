flank_5 = "CATTATTTTCACTTGGGTCGAGGCCAGATTCCATC"
flank_3 = "GGATTGCCCGAAATCAGAGAAAAGTCG"
snp_notation = "[G/A]"
iupac_snp = "R"

length_5_prime = len(flank_5)
length_3_prime = len(flank_3)
region = flank_5 + snp_notation + flank_3
region_iupac = flank_5 + iupac_snp + flank_3
snp_from_region = region[length_5_prime : length_5_prime + len(snp_notation)]
snp_from_iupac = region_iupac[length_5_prime]

print(f"Довжина 5’ флангової області: {length_5_prime}.")
print(f"Довжина 3’ флангової області: {length_3_prime}.")
print("\nПослідовність 'region' (з нотацією [G/A]):")
print(region)
print("Послідовність 'region_iupac' (з нотацією R):")
print(region_iupac)
print(f"\nОтриманий SNP з 'region' ([G/A]): {snp_from_region}")
print(f"Отриманий SNP з 'region_iupac' (R): {snp_from_iupac}")