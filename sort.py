# 3. Преобразование CSV
import pandas as pd
import os

input_folder = 'CSV'
output_folder = 'CSV'

for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.csv'):
            csv_file = os.path.join(root, file)
            df = pd.read_csv(csv_file, header=None)
            new_rows = []

            for index, row in df.iterrows():
                if len(row) >= 6:
                    new_rows.append([row[0], row[1], row[2]])
                    new_rows.append([row[3], row[4], row[5]])

            new_df = pd.DataFrame(new_rows)
            new_csv_file = os.path.join(output_folder, os.path.relpath(csv_file, input_folder))
            os.makedirs(os.path.dirname(new_csv_file), exist_ok=True)
            new_df.to_csv(new_csv_file, index=False, header=False)
