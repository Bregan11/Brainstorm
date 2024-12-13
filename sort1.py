# 4. Сортировка по численным значениям в CSV
import pandas as pd
import os

input_folder = 'CSV'

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.csv'):
            csv_file = os.path.join(root, file)
            df = pd.read_csv(csv_file, header=None)
            df = df.sort_values(by=[0])
            df.to_csv(csv_file, index=False, header=False)
