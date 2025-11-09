import re
def analyze_schedule(filename):
    subjects = set()
    lectures = labs = practicals = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            match = re.match(r"(.+)\((лекція|лабораторна|практична)\)", line)
            if match:
                subject = match.group(1).strip()
                lesson_type = match.group(2).strip().lower()
                subjects.add(subject)
                if lesson_type == "лекція":
                    lectures += 1
                elif lesson_type == "лабораторна":
                    labs += 1
                elif lesson_type == "практична":
                    practicals += 1
    print(f"Кількість різних предметів: {len(subjects)}")
    print(f"Лекцій: {lectures}, Лабораторних: {labs}, Практичних: {practicals}")
analyze_schedule("rozklad.txt")
