from pathlib import Path

def total_salary():
    file_path = Path("salaries.txt")

    if not file_path.exists():
        print(f"Файл {file_path} не знайдено.")
        return None

    if file_path.stat().st_size == 0:
        print(f"Файл {file_path} порожній")
        return None

    count = 0
    total = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) == 2:
                try:
                    salary = int(parts[1])
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Неправильний формат зарплати: {parts[1]}")
            else:
                print(f"Неправильний формат рядка: {line}")

    average = total / count if count > 0 else 0
    return total, average

result = total_salary()
if result:
    total, average = result
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
