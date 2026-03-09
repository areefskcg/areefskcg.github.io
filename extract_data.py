import pandas as pd
import json

xl = pd.ExcelFile(r'Copilot_License (3).xlsx')
all_data = {}

for sheet in xl.sheet_names:
    print(f'Reading sheet: {sheet}')
    df = pd.read_excel(xl, sheet_name=sheet)
    # Clean the dataframe - drop rows/cols that are all NaN
    df = df.dropna(how='all').dropna(axis=1, how='all')
    all_data[sheet] = {
        'columns': df.columns.tolist(),
        'shape': list(df.shape),
        'data': df.fillna('').to_dict('records')
    }
    print(f'  - Shape: {df.shape}')
    print(f'  - Columns: {df.columns.tolist()}')

# Save as JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=2, default=str)

print('\nData exported to data.json')
