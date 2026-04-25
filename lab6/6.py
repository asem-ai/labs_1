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

#4 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
electronics_expensive = df[(df['col_2'] > 500) & (df['col_7'] == "Electronics")]
print(electronics_expensive.head())

#5 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
grouped = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    max_price=('col_2', 'max'),
    total_quantity=('col_3', 'sum')
).reset_index()
grouped = grouped.rename(columns={'col_7': 'category'})
print(grouped)

#6 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
numeric_cols = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6',
                'col_7', 'col_8', 'col_9', 'col_10', 'col_11']
stats = []
for col in numeric_cols:
    stats.append({
        'column': col,
        'mean': df[col].mean(),
        'median': df[col].median(),
        'std': df[col].std()
    })
stats_df = pd.DataFrame(stats)
print(stats_df)

#7 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()
threshold = mean_price + 3 * std_price
anomalies = df[df['col_2'] > threshold]
print(f"Средняя цена: {mean_price:.2f}")
print(f"Стандартное отклонение: {std_price:.2f}")
print(f"Порог (среднее + 3σ): {threshold:.2f}")
print(f"\nКоличество аномальных товаров: {len(anomalies)}")
print("\nПервые 5 строк аномальных товаров:")
print(anomalies[['col_2']].head())

#8 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
numeric_cols = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6',
                'col_7', 'col_8', 'col_9', 'col_10', 'col_11']
correlation_matrix = df[numeric_cols].corr()
corr_df = pd.DataFrame(correlation_matrix)
print("Корреляционная матрица для колонок col_2 - col_11:")
print(corr_df)
