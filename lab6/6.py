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

#9 task
import matplotlib.pyplot as plt
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
plt.figure(figsize=(10, 6))
plt.hist(df['col_2'].dropna(), bins=50, edgecolor='black', alpha=0.7)
plt.title('Распределение цен товаров', fontsize=14)
plt.xlabel('Цена товара', fontsize=12)
plt.ylabel('Количество товаров', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

#10 task
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df_clean = df[['col_2', 'col_3']].dropna()
plt.figure(figsize=(10, 6))
sns.regplot(x='col_2', y='col_3', data=df_clean, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Зависимость между ценой и количеством на складе', fontsize=14)
plt.xlabel('Цена товара (col_2)', fontsize=12)
plt.ylabel('Количество на складе (col_3)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()
correlation = df_clean['col_2'].corr(df_clean['col_3'])
print(f"Коэффициент корреляции Пирсона: {correlation:.3f}")

#11 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df_clean = df[['col_7', 'col_2']].dropna()
plt.figure(figsize=(12, 6))
sns.boxplot(x='col_7', y='col_2', data=df_clean)
plt.title('Распределение цен по категориям товаров', fontsize=14)
plt.xlabel('Категория товара', fontsize=12)
plt.ylabel('Цена товара', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

#12 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df_clean = df[['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']].dropna()
sns.pairplot(df_clean, vars=['col_2', 'col_3', 'col_4', 'col_5', 'col_6'],
             hue='col_7', diag_kind='hist', plot_kws={'alpha':0.6})
plt.suptitle('Парные диаграммы для числовых колонок с разделением по категориям',
             y=1.02, fontsize=14)
plt.show()

#13 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
numeric_cols = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6',
                'col_7', 'col_8', 'col_9', 'col_10', 'col_11']
corr_matrix = df[numeric_cols].corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix,
            annot=True,
            cmap='coolwarm',
            center=0,
            fmt='.2f',
            square=True,
            linewidths=0.5,
            cbar_kws={'shrink': 0.8})
plt.title('Тепловая карта корреляции числовых характеристик товаров', fontsize=14, pad=20)
plt.tight_layout()
plt.show()