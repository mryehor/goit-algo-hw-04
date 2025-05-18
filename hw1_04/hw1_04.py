from pathlib import Path 
def total_salary(path):
    count = 0
    total = 0
    file_path = Path(path)
    if not file_path.exists():
        print(f"Файл {path} не знайдено.")
        return 0, 0
    if file_path.stat().st_size == 0:
        print(f"Файл {path} порожній")
        return 0,0
        
    with open("path.txt", "r" ) as file:
        for lines in file:
            lines = lines.strip()
            if not lines:
                continue
            parts = lines.split(",")
            if len(parts) == 2:
                try:
                    salary = int(parts[1])
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Неправильний формат зарплати: {parts[1]}")
        average = total/count if count > 0 else 0 
        return total, average
with open("path.txt", "w+" ) as file:
        file.write("")
result = total_salary("path.txt")      
if result:
    total , average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")