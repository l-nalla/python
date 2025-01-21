import pandas as pd
import json
file_path = 'sample.json'
df = pd.read_json(file_path)

df.to_csv("sample.csv", index=False)

print(df.describe())