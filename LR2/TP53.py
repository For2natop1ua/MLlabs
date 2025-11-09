chain_a = """SSSVPSQKTYQGSYGFRLGFLHSGTAKSVTCTYSPALNKM
FCQLAKTCPVQLWVDSTPPPGTRVRAMAIYKQSQHMTEVV
RRCPHHERCSDSDGLAPPQHLIRVEGNLRVEYLDDRNTFR
HSVVVPYEPPEVGSDCTTIHYNYMCNSSCMGGMNRRPILT
IITLEDSSGNLLGRNSFEVRVCACPGRDRRTEEENLRKKG
EPHHELPPGSTKRALPNNT"""
lines_count = len(chain_a.split('\n'))
sequence_no_newlines = chain_a.replace('\n', '')
sequence_length = len(sequence_no_newlines)
c_count = sequence_no_newlines.count('C')
h_count = sequence_no_newlines.count('H')
subseq = "NLRVEYLDDRN"
subseq_index = sequence_no_newlines.find(subseq)
first_line_end = chain_a.find('\n')
first_line = chain_a[:first_line_end]
print(f"Кількість рядків: {lines_count}")
print(f"Довжина послідовності: {sequence_length}")
print(f"Послідовність без нових рядків:\n{sequence_no_newlines}")
print(f"Кількість цистеїнів 'C': {c_count}")
print(f"Кількість гістидинів 'H': {h_count}")
if subseq_index != -1:
    print(f"Підпослідовність '{subseq}' знайдена на позиції: {subseq_index}")
else:
    print(f"Підпослідовність '{subseq}' не знайдена")
print(f"Перший рядок послідовності:\n{first_line}")