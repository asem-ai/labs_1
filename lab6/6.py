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

#12 task=43 task
#13 task
df_13 = df[[f'col_{i}' for i in range(2, 12)]].apply(pd.to_numeric, errors='coerce')
corr_matrix = df_13.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Тепловая карта корреляции характеристик товаров (col_2-col_11)', fontsize=15)
plt.show()

#14 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['total_value'] = df['col_2'] * df['col_3']
df['double_stock'] = df['col_4'] * 2
df['log_price'] = np.log(df['col_2'])
columns_to_save = list(df.columns)
df.to_excel('catalog_analysis.xlsx', index=False)
print("Файл успешно сохранен как 'catalog_analysis.xlsx'")
print(f"Размер сохраненного DataFrame: {df.shape}")
print(f"Количество колонок: {len(df.columns)}")
print("\nСписок всех колонок в сохраненном файле:")
print(df.columns.tolist())

#15 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['log_price'] = np.log(df['col_2'])
category_summary = df.groupby('col_7').agg(
    count=('col_2', 'count'),
    mean_price=('col_2', 'mean'),
    total_quantity=('col_3', 'sum'),
    mean_log_price=('log_price', 'mean')
).reset_index()
category_summary = category_summary.rename(columns={'col_7': 'category'})
print("Финальный агрегированный отчет по категориям:")
print(category_summary)

#16 task
import pandas as pd
df['col_2'] = pd.to_numeric(df['col_2'], errors='coerce')
idx = df.groupby('col_7')['col_2'].idxmax()
most_expensive = df.loc[idx, ['col_1', 'col_2', 'col_7']]
print("#16")
print(most_expensive)
#17 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['total_value'] = df['col_2'] * df['col_3']
df_sorted = df.sort_values('total_value', ascending=False)
top_10 = df_sorted[['col_1', 'col_2', 'col_3', 'total_value']].head(10)
top_10 = top_10.rename(columns={
    'col_1': 'товар',
    'col_2': 'цена',
    'col_3': 'количество',
    'total_value': 'общая_стоимость'
})
print("Топ-10 товаров по общей стоимости на складе:")
print(top_10)
top_10.to_excel('top_10_total_value.xlsx', index=False)

#18 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df_clean = df[['col_2']].dropna()
def price_range(price):
    if price <= 50:
        return 'до 50'
    elif price <= 200:
        return '50-200'
    elif price <= 500:
        return '200-500'
    elif price <= 1000:
        return '500-1000'
    else:
        return 'больше 1000'
df_clean['price_range'] = df_clean['col_2'].apply(price_range)
price_counts = df_clean['price_range'].value_counts().reset_index()
price_counts.columns = ['price_range', 'count']
order = ['до 50', '50-200', '200-500', '500-1000', 'больше 1000']
price_counts['price_range'] = pd.Categorical(price_counts['price_range'], categories=order, ordered=True)
price_counts = price_counts.sort_values('price_range')
print("Распределение товаров по ценовым диапазонам:")
print(price_counts)
plt.figure(figsize=(10, 6))
sns.barplot(data=price_counts, x='price_range', y='count', hue='price_range', palette='Blues_d', legend=False)
plt.title('Распределение товаров по ценовым диапазонам', fontsize=14)
plt.xlabel('Ценовой диапазон', fontsize=12)
plt.ylabel('Количество товаров', fontsize=12)
for i, row in price_counts.iterrows():
    plt.text(i, row['count'] + 10, str(row['count']), ha='center', fontsize=10)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

#19 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df['total_value'] = df['col_2'] * df['col_3']
category_value = df.groupby('col_7')['total_value'].sum().reset_index()
category_value = category_value.dropna()  # NaN жою
category_value_sorted = category_value.sort_values('total_value', ascending=False)
if len(category_value_sorted) > 0:
    top_category = category_value_sorted.iloc[0]
    print("Ең үлкен категория:", top_category['col_7'])
    print("Суммарная стоимость:", top_category['total_value'])
else:
    print("Қате: Деректер табылмады!")
    print("Себептері:")
    print("- 'col_7' бағаны жоқ")
    print("- 'col_7' бағанында барлық мәндер NaN")
    print("- 'col_2' немесе 'col_3' бағандарында деректер жоқ")
#20 task= 36 task
#21 task= 37 task
#22 task=38 task
#23 task=39 task
#24 task=40 task
#25 task=41 task
#36 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
category_stats = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    mean_quantity=('col_3', 'mean')
).reset_index()
category_stats = category_stats.rename(columns={'col_7': 'category'})
category_stats = category_stats.dropna()
print("Средняя цена и средний запас по категориям:")
print(category_stats)
print("\n" + "="*50 + "\n")
plt.figure(figsize=(10, 8))
scatter = sns.scatterplot(
    data=category_stats,
    x='mean_price',
    y='mean_quantity',
    hue='category',
    s=250,
    palette='Set2'
)
for i, row in category_stats.iterrows():
    plt.annotate(
        row['category'],
        (row['mean_price'], row['mean_quantity']),
        xytext=(8, 8),
        textcoords='offset points',
        fontsize=10,
        fontweight='bold'
    )
plt.title('Сравнение категорий по средней цене и среднему запасу', fontsize=14)
plt.xlabel('Средняя цена', fontsize=12)
plt.ylabel('Средний запас', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(title='Категория', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

#37 task=21 task
price_variation = df.groupby('col_7')['col_2'].std().reset_index()
price_variation.columns = ['category', 'std_price']
sns.barplot(data=price_variation.sort_values('std_price', ascending=False),
            x='std_price', y='category', hue='category', palette='magma', legend=False)
plt.title('Разброс цен (стандартное отклонение) по категориям')
plt.xlabel('Стандартное отклонение цены')
plt.ylabel('Категория')
plt.show()
print("#21")
print(price_variation)

#38 task=22 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
zero_stock = df[df['col_3'] == 0]
zero_stock_products = zero_stock[['col_1', 'col_7', 'col_2']].dropna()
print("Товары с нулевым запасом (первые 10):")
print(zero_stock_products.head(10))
print(f"\nВсего товаров с нулевым запасом: {len(zero_stock_products)}")

#39 task=23 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
category_count = df.groupby('col_7').size().reset_index(name='count')
category_count = category_count.rename(columns={'col_7': 'category'})
category_count = category_count.dropna()
top_5_categories = category_count.sort_values('count', ascending=False).head(5)
print("Топ-5 категорий по количеству товаров:")
print(top_5_categories)
print("\n" + "="*50 + "\n")
plt.figure(figsize=(10, 6))
sns.barplot(data=price_counts, x='price_range', y='count', hue='price_range', palette='Blues_d', legend=False)
plt.title('Топ-5 категорий по количеству товаров', fontsize=14)
plt.xlabel('Категория', fontsize=12)
plt.ylabel('Количество товаров', fontsize=12)
for i, row in top_5_categories.iterrows():
    plt.text(i, row['count'] + 50, str(row['count']), ha='center', fontsize=10)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

#40 task=24 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df_sorted = df.sort_values('col_3', ascending=False)
top_10_stock = df_sorted[['col_1', 'col_3']].head(10)
top_10_stock = top_10_stock.dropna()
print("Топ-10 товаров по количеству на складе:")
print(top_10_stock)
print("\n" + "="*50 + "\n")
plt.figure(figsize=(12, 8))
sns.barplot(
    data=top_10_stock,
    y='col_1',
    x='col_3',
    hue='col_1',
    palette='Blues_d',
    legend=False
)
plt.title('Топ-10 товаров по количеству на складе', fontsize=14)
plt.xlabel('Количество на складе', fontsize=12)
plt.ylabel('Название товара', fontsize=12)
for i, row in top_10_stock.iterrows():
    plt.text(row['col_3'] + 5, i, str(int(row['col_3'])),
             va='center', fontsize=9)
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

#41 task=25 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df_clean = df[['col_7', 'col_2']].dropna()
def price_range(price):
    if price <= 50:
        return 'до 50'
    elif price <= 200:
        return '50-200'
    elif price <= 500:
        return '200-500'
    elif price <= 1000:
        return '500-1000'
    else:
        return '>1000'
df_clean['price_range'] = df_clean['col_2'].apply(price_range)
order = ['до 50', '50-200', '200-500', '500-1000', '>1000']
df_clean['price_range'] = pd.Categorical(df_clean['price_range'], categories=order, ordered=True)
pivot_table = pd.pivot_table(
    df_clean,
    values='col_2',
    index='col_7',
    columns='price_range',
    aggfunc='count',
    fill_value=0
)
pivot_table.index.name = 'category'
print("Сводная таблица: распределение товаров по категориям и ценовым диапазонам")
print(pivot_table)
print("\n" + "="*50 + "\n")
plt.figure(figsize=(12, 8))
sns.heatmap(
    pivot_table,
    annot=True,
    fmt='d',
    cmap='YlOrRd',
    linewidths=0.5,
    cbar_kws={'label': 'Количество товаров'}
)
plt.title('Тепловая карта: Распределение товаров по категориям и ценовым диапазонам', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#42 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df_clean = df[['col_2', 'col_5']].dropna()
correlation = df_clean['col_2'].corr(df_clean['col_5'])
print(f"Коэффициент корреляции Пирсона: {correlation:.3f}")
print("\n" + "="*50 + "\n")
plt.figure(figsize=(10, 6))
sns.regplot(
    x='col_2',
    y='col_5',
    data=df_clean,
    scatter_kws={'alpha': 0.5, 's': 30},
    line_kws={'color': 'red', 'linewidth': 2}
)
plt.title('Зависимость между ценой и рейтингом товаров', fontsize=14)
plt.xlabel('Цена товара (col_2)', fontsize=12)
plt.ylabel('Рейтинг товара (col_5)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.annotate(
    f'Корреляция = {correlation:.3f}',
    xy=(0.05, 0.95),
    xycoords='axes fraction',
    fontsize=12,
    bbox=dict(boxstyle="round", facecolor='white', alpha=0.8)
)
plt.tight_layout()
plt.show()

#43 task=12 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
df_plot = df[['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7']].copy()
df_plot = df_plot.dropna()
df_plot = df_plot.rename(columns={
    'col_2': 'Цена',
    'col_3': 'Запас',
    'col_4': 'Продажи',
    'col_5': 'Рейтинг',
    'col_6': 'Скидка',
    'col_7': 'Категория'
})
print("Данные для анализа:")
print(df_plot.head())
print(f"\nРазмер данных: {df_plot.shape}")
print("\n" + "="*50 + "\n")
pairplot = sns.pairplot(
    df_plot,
    vars=['Цена', 'Запас', 'Продажи', 'Рейтинг', 'Скидка'],
    hue='Категория',
    diag_kind='hist',
    plot_kws={'alpha': 0.6, 's': 30},
    palette='Set2'
)
pairplot.fig.suptitle('Парные диаграммы числовых характеристик товаров',
                       y=1.02, fontsize=14)
plt.tight_layout()
plt.show()
print("\nСтатистика по числовым колонкам:")
print(df_plot[['Цена', 'Запас', 'Продажи', 'Рейтинг', 'Скидка']].describe())
print("\nКорреляционная матрица:")
print(df_plot[['Цена', 'Запас', 'Продажи', 'Рейтинг', 'Скидка']].corr())

#44 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()
mean_stock = df['col_3'].mean()
std_stock = df['col_3'].std()
threshold_price = mean_price + 3 * std_price
threshold_stock = mean_stock + 3 * std_stock
extreme_items = df[(df['col_2'] > threshold_price) | (df['col_3'] > threshold_stock)]
print(f"Аномальных товаров: {len(extreme_items)}")
print(extreme_items[['col_1', 'col_2', 'col_3', 'col_7']].head(10))

#35 task
df = pd.read_excel('catalog_products.xlsx')
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')
if 'col_7' not in df.columns:
    print("Қате: 'col_7' бағаны жоқ!")
    print("Бар бағандар:", df.columns.tolist())
    exit()
if df['col_7'].isnull().all():
    print("Қате: 'col_7' бағанында барлық мәндер NaN!")
    exit()
df['total_value'] = df['col_2'] * df['col_3']
category_total = df.groupby('col_7')['total_value'].sum().reset_index()
category_total = category_total.dropna()
if len(category_total) > 0:
    category_total = category_total.sort_values('total_value', ascending=False)
    print("ЕҢ ҮЛКЕН КАТЕГОРИЯ:", category_total.iloc[0]['col_7'])
    print("ҚҰНЫ:", category_total.iloc[0]['total_value'])
    plt.figure(figsize=(10, 6))
    sns.barplot(data=category_total, x='col_7', y='total_value', hue='col_7', legend=False)
    plt.xticks(rotation=45)
    plt.title('Категориялар бойынша жалпы құн')
    plt.tight_layout()
    plt.show()
else:
    print("Категория бойынша деректер жоқ!")