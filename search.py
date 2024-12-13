# 6. Поиск по группе преподавателя и кабинету
import pandas as pd
import os

group = input("Введите группу: ")
input_folder = 'CSV'

results = []

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.csv'):
            csv_file = os.path.join(root, file)
            df = pd.read_csv(csv_file, header=None)
            matches = df[df[1].str.contains(group, na=False)]
            if not matches.empty:
                results.append((os.path.basename(root), file.replace('.csv', ''), matches))

# Вывод результатов
for folder_name, file_name, matches in results:
    print(f"Дата: {folder_name}")
    print(f"{file_name}")
    for index, row in matches.iterrows():
        print(f"Кабинет: {row[0]}, Группа: {row[1]}, Преподаватель: {row[2]}")
    print("-" * 20)
