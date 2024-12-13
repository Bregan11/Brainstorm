# 2. Преобразование xlsx в csv
import pandas as pd
import os

input_folder = '/workspaces/Brainstorm/Загрузки'
output_folder = 'CSV'

for filename in os.listdir(input_folder):
    if filename.endswith('.xlsx'):
        xlsx_file = os.path.join(input_folder, filename)
        xls = pd.ExcelFile(xlsx_file)
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
            csv_file = os.path.join(output_folder, filename.replace('.xlsx', ''), f'{sheet_name}.csv')
            os.makedirs(os.path.dirname(csv_file), exist_ok=True)
            df.to_csv(csv_file, index=False)
