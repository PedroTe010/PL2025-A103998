import re
from collections import defaultdict

def clean_description(text):
    return re.sub(r"\s+", " ", text).strip()

def fix_csv_in_memory(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        header = file.readline().strip()
        lines = [header]

        temp_line = ""
        for line in file:
            line = line.strip()
            
            if temp_line:
                temp_line += " " + line
            else:
                temp_line = line
            
            if temp_line.count(";") >= 6:
                parts = temp_line.split(";")
                if len(parts) >= 7: 
                    parts[1] = clean_description(parts[1])
                    lines.append(";".join(parts))
                temp_line = ""
    
    return lines

def process_csv_data(csv_data):
    composers = set()
    period_counts = defaultdict(int)
    period_titles = defaultdict(list)
    
    header = csv_data[0].split(";")

    for line in csv_data[1:]:
        parts = line.split(";")
        
        diff = len(parts) - 7
        nome, periodo, compositor = parts[0].strip(), parts[3+diff].strip(), parts[4+diff].strip()
        
        if not nome or not periodo or not compositor:
            print(f"Linha ignorada: {line}")
            continue
        
        composers.add(compositor)
        period_counts[periodo] += 1
        period_titles[periodo].append(nome)
    
    sorted_composers = sorted(composers)
    sorted_period_titles = {k: sorted(v) for k, v in period_titles.items()}
    
    return sorted_composers, dict(period_counts), sorted_period_titles

csv_data = fix_csv_in_memory("obras.csv")
sorted_composers, period_counts, sorted_period_titles = process_csv_data(csv_data)

print("Lista de compositores ordenada:", sorted_composers)
print("Distribuição das obras por período:", period_counts)
print("Dicionário de obras por período:", sorted_period_titles)