#1 task
import pandas as pd
df = pd.read_excel('catalog_products.xlsx')
print("Форма DataFrame:", df.shape)
print("\nТиптері:")
print(df.dtypes)
print("\nПропусктер саны:")
print(df.isnull().sum())
print("\nАлғашқы 5 жол:")
print(df.head())

#2 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
numeric_cols = df.columns[df.isnull().sum() < len(df)].tolist()
for col in numeric_cols:
    if df[col].isnull().sum() > 0:
        mean_val = df[col].mean()
        df[col].fillna(mean_val, inplace=True)
print("Проверка пропусков в числовых колонках:")
for col in numeric_cols:
    missing = df[col].isnull().sum()
    print(f"{col}: {missing} пропусков")
print("\nПервые 5 строк числовых колонок:")
print(df[numeric_cols].head())

#3 task
import pandas as pd
import numpy as np
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_4'] * 2
df['log_price'] = np.log(df['col_2'])
print("Новые колонки (первые 5 строк):")
print(df[['col_2', 'col_3', 'col_4', 'total_value', 'double_stock', 'log_price']].head())