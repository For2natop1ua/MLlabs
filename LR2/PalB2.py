gene_extract = """CTGTCTCCCTCACTGTATGTAAATTGCATCTAGAATAGCA
TCTGGAGCACTAATTGACACATAGTGGGTATCAATTATTA
TTCCAGGTACTAGAGATACCTGGACCATTAACGGATAAAT
AGAAGATTCATTTGTTGAGTGACTGAGGATGGCAGTTCCT
GCTACCTTCAAGGATCTGGATGATGGGGAGAAACAGAGAA
CATAGTGTGAGAATACTGTGGTAAGGAAAGTACAGAGGAC
TGGTAGAGTGTCTAACCTAGATTTGGAGAAGGACCTAGAA
GTCTATCCCAGGGAAATAAAAATCTAAGCTAAGGTTTGAG
GAATCAGTAGGAATTGGCAAAGGAAGGACATGTTCCAGAT
GATAGGAACAGGTTATGCAAAGATCCTGAAATGGTCAGAG
CTTGGTGCTTTTTGAGAACCAAAAGTAGATTGTTATGGAC
CAGTGCTACTCCCTGCCTCTTGCCAAGGGACCCCGCCAAG
CACTGCATCCCTTCCCTCTGACTCCACCTTTCCACTTGCC CAGTATTGTTGGTGT"""

clean_dna = gene_extract.replace('\n', '').replace(' ', '')
mrna = clean_dna.replace('T', 'U')
uracil_count = mrna.count('U')
total_length = len(mrna)
genetic_code = {
    'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
    'UGG': 'Trp'
}
stop_codons = []
glycine_codons = []
tryptophan_codons = []

for frame in range(3):
    for i in range(frame, len(mrna) - 2, 3):
        codon = mrna[i:i+3]
        amino_acid = genetic_code.get(codon, 'Other')

        if amino_acid == 'STOP':
            stop_codons.append({'codon': codon, 'position': i, 'frame': frame})
        elif amino_acid == 'Gly':
            glycine_codons.append({'codon': codon, 'position': i, 'frame': frame})
        elif amino_acid == 'Trp':
            tryptophan_codons.append({'codon': codon, 'position': i, 'frame': frame})

is_trp_present = "Так" if tryptophan_codons else "Ні"
print(f"Довжина послідовності мРНК: {total_length}")
print(f"Кількість урацилів (U): {uracil_count}")
print(f"Скільки стоп-кодонів присутні в послідовності? {len(stop_codons)}")
print(f"Скільки гліцинів (Gly)? {len(glycine_codons)}")
print(f"Чи присутній триптофан (Trp)? {is_trp_present}")

if tryptophan_codons:
    leftmost_trp = min(tryptophan_codons, key=lambda x: x['position'])
    rightmost_trp = max(tryptophan_codons, key=lambda x: x['position'])
    print(f"Позиція крайнього лівого Trp: {leftmost_trp['position']} (рамка {leftmost_trp['frame'] + 1})")
    print(f"Кодон (для перевірки): {leftmost_trp['codon']}")
    print(f"Позиція крайнього правого Trp: {rightmost_trp['position']} (рамка {rightmost_trp['frame'] + 1})")
    print(f"Кодон (для перевірки): {rightmost_trp['codon']}")
else:
    print("Триптофан (Trp) не знайдено.")
