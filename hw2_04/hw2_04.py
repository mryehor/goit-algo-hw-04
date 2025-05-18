#Вимоги до завдання:

#Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
#Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
#Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


#Рекомендації для виконання:

#Використовуйте with для безпечного читання файлу.
#Пам'ятайте про встановлення кодування при відкриті файлів
#Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
#Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
#Опрацьовуйте можливі винятки, пов'язані з читанням файлу.

from pathlib import Path
def get_cats_info(path): 
    file_path = Path(path)
    if not file_path.exists():
        print(f"Файл {path} не знайдено.")
        return []
    if file_path.stat().st_size == 0:
        print(f"Файл {path} порожній")
        return []
    cats_info = []
    with open(path, "r") as file:
        for lines in file:
            lines = lines.strip()
            if not lines:
                continue
            parts = lines.split(",")
            if len(parts) == 3:
                cat_dict = {
                    "id" : parts[0],
                    "name" : parts[1],
                    "age" : parts[2]
                }
                cats_info.append(cat_dict)
        return cats_info
with open("path.txt", "w") as file:
    file.write("60b90c1c13067a15887e1ae1,Tayson,3\n"
               "60b90c2413067a15887e1ae2,Vika,1\n"
               "60b90c2e13067a15887e1ae3,Barsik,2\n"
               "60b90c3b13067a15887e1ae4,Simon,12\n"
               "60b90c4613067a15887e1ae5,Tessi,5")
    
info = get_cats_info("path.txt")
print(info)