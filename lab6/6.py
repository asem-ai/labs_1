# АЛДЫН АЛА ҚАДАМ: КІТАПХАНАЛАРДЫ ҚОСУ
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ескерту хабарламаларын өшіру
import warnings
warnings.filterwarnings('ignore')

# 1-ЕСЕП: ФАЙЛДЫ ЖҮКТЕУ ЖӘНЕ ТЕКСЕРУ
print("="*50)
print("1-ЕСЕП: ФАЙЛДЫ ТЕКСЕРУ")
print("="*50)

# ЖАСАНДЫ ДЕРЕКТЕР ЖАСАУ (файл жоқ болғандықтан)
# Нақты файлыңыз болса: df = pd.read_excel('catalog_products.xlsx')

# 10000 жол, 50 баған жасаймыз
np.random.seed(42)
n = 10000

df = pd.DataFrame({
    'col_1': [f'Тауар_{i}' for i in range(1, n+1)],  # тауар аты
    'col_2': np.random.randint(10, 5000, n),          # бағасы (10-5000тг)
    'col_3': np.random.randint(0, 500, n),            # саны (0-500 дана)
    'col_4': np.random.randint(1, 100, n),            # басқа сан
    'col_5': np.random.uniform(1, 5, n).round(1),     # рейтинг (1-5)
    'col_6': np.random.randint(0, 1000, n),           # сатылым саны
    'col_7': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], n),  # категория
    'col_8': np.random.uniform(0, 0.3, n).round(2),   # жеңілдік (0-30%)
    'col_9': np.random.randint(1, 13, n),             # ай (1-12)
    'col_10': np.random.choice(['A', 'B', 'C'], n),   # сегмент
})

# Қалған 40 бағанды қосу (маңызды емес)
for i in range(11, 51):
    df[f'col_{i}'] = np.random.randn(n)

# Кейбір пропустар қосу (бос орындар)
for col in ['col_2', 'col_3', 'col_5']:
    mask = np.random.random(n) < 0.02  # 2% бос орын
    df.loc[mask, col] = np.nan

print(f"1. Кесте өлшемі: {df.shape[0]} жол, {df.shape[1]} баған")
print(f"\n2. Баған типтері:")
print(df.dtypes.value_counts())
print(f"\n3. Пропустар (бос орындар):")
print(df.isnull().sum()[df.isnull().sum() > 0])
print(f"\n4. Алғашқы 5 жол:")
print(df.head())

# 2-ЕСЕП: САНДАРДЫ ТҮЗЕТУ
print("\n" + "="*50)
print("2-ЕСЕП: САНДАРДЫ ТҮЗЕТУ")
print("="*50)

# Сандық бағандардың тізімі
сандық_бағандар = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_8', 'col_9']

for баған in сандық_бағандар:
    # Мәтінді санға айналдыру
    df[баған] = pd.to_numeric(df[баған], errors='coerce')
    # Пропустарды орташа мәнмен толтыру
    орташа = df[баған].mean()
    df[баған] = df[баған].fillna(орташа)

print("Сандық бағандар түзетілді!")
print(f"Пропустар қалды ма? {df[сандық_бағандар].isnull().sum().sum() == 0}")

# 3-ЕСЕП: ЖАҢА БАҒАНДАР ҚОСУ
print("\n" + "="*50)
print("3-ЕСЕП: ЖАҢА БАҒАНДАР ҚОСУ")
print("="*50)

# Жалпы құн = баға × саны
df['total_value'] = df['col_2'] * df['col_3']

# Екі еселенген қор = саны × 2
df['double_stock'] = df['col_3'] * 2

# Логарифмдік баға
df['log_price'] = np.log(df['col_2'])

print("Жаңа бағандар қосылды:")
print(f"- total_value (баға × саны)")
print(f"- double_stock (саны × 2)")
print(f"- log_price (log(баға))")

print("\nҮЛГІ:")
print(df[['col_2', 'col_3', 'total_value', 'double_stock', 'log_price']].head())

# 4-ЕСЕП: ЭЛЕКТРОНИКАНЫҢ ҚЫМБАТ ТАУАРЛАРЫ
print("\n" + "="*50)
print("4-ЕСЕП: ҚЫМБАТ ЭЛЕКТРОНИКА")
print("="*50)

# Бағасы 500-ден жоғары ЖӘНЕ категориясы Electronics
электроника_қымбат = df[(df['col_2'] > 500) & (df['col_7'] == 'Electronics')]

print(f"Табылды: {len(электроника_қымбат)} тауар")
print(электроника_қымбат[['col_1', 'col_2', 'col_7']].head())

# 5-ЕСЕП: КАТЕГОРИЯ БОЙЫНША СТАТИСТИКА
print("\n" + "="*50)
print("5-ЕСЕП: КАТЕГОРИЯ СТАТИСТИКАСЫ")
print("="*50)

категория_стат = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),      # орташа баға
    max_price=('col_2', 'max'),        # ең қымбаты
    total_quantity=('col_3', 'sum')    # жалпы саны
).round(2)

print(категория_стат)

# 6-ЕСЕП: 10 БАҒАННЫҢ СТАТИСТИКАСЫ
print("\n" + "="*50)
print("6-ЕСЕП: САНДЫҚ БАҒАНДАР СТАТИСТИКАСЫ")
print("="*50)

# Алғашқы 10 сандық баған
алғашқы_10_сан = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_8', 'col_9', 'col_11', 'col_12', 'col_13']

статистика_кестесі = pd.DataFrame({
    'column': алғашқы_10_сан,
    'mean': [df[col].mean() for col in алғашқы_10_сан],
    'median': [df[col].median() for col in алғашқы_10_сан],
    'std': [df[col].std() for col in алғашқы_10_сан]
}).round(2)

print(статистика_кестесі)

# 7-ЕСЕП: АНОМАЛИЯЛЫ ТАУАРЛАР
print("\n" + "="*50)
print("7-ЕСЕП: АНОМАЛИЯЛЫ ҚЫМБАТ ТАУАРЛАР")
print("="*50)

орташа = df['col_2'].mean()
стандарт_ауытқу = df['col_2'].std()
шекара = орташа + 3 * стандарт_ауытқу

аномалиялар = df[df['col_2'] > шекара]
print(f"Орташа баға: {орташа:.2f}")
print(f"Шекара: {шекара:.2f}")
print(f"Аномалиялар саны: {len(аномалиялар)}")
print(аномалиялар[['col_1', 'col_2', 'col_7']].head())

# 8-ЕСЕП: КОРРЕЛЯЦИЯ МАТРИЦАСЫ
print("\n" + "="*50)
print("8-ЕСЕП: КОРРЕЛЯЦИЯ МАТРИЦАСЫ")
print("="*50)

корреляция = df[алғашқы_10_сан].corr()
print(корреляция.round(2))

# 9-ЕСЕП: БАҒАНЫҢ ГИСТОГРАММАСЫ
print("\n" + "="*50)
print("9-ЕСЕП: БАҒА ГИСТОГРАММАСЫ")
print("="*50)

plt.figure(figsize=(10, 6))
plt.hist(df['col_2'], bins=50, color='steelblue', edgecolor='black')
plt.title('Тауарлардың Баға Бойынша Бөлінуі', fontsize=14)
plt.xlabel('Баға (тг)', fontsize=12)
plt.ylabel('Тауарлар саны', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# 10-ЕСЕП: БАҒА МЕН САННЫҢ БАЙЛАНЫСЫ
print("\n" + "="*50)
print("10-ЕСЕП: БАҒА МЕН САННЫҢ БАЙЛАНЫСЫ")
print("="*50)

plt.figure(figsize=(10, 6))
sns.regplot(x=df['col_2'], y=df['col_3'], scatter_kws={'alpha':0.3}, line_kws={'color':'red'})
plt.title('Баға мен Тауар Санының Байланысы', fontsize=14)
plt.xlabel('Баға (тг)', fontsize=12)
plt.ylabel('Қоймадағы саны', fontsize=12)
plt.show()

# 11-ЕСЕП: КАТЕГОРИЯ БОЙЫНША БАҒА (BOXPLOT)
print("\n" + "="*50)
print("11-ЕСЕП: КАТЕГОРИЯ БОЙЫНША БАҒА")
print("="*50)

plt.figure(figsize=(12, 6))
sns.boxplot(x='col_7', y='col_2', data=df)
plt.title('Категориялар Бойынша Бағаның Бөлінуі', fontsize=14)
plt.xlabel('Категория', fontsize=12)
plt.ylabel('Баға (тг)', fontsize=12)
plt.xticks(rotation=45)
plt.show()

# 12-ЕСЕП: ПАРЛЫ ДИАГРАММАЛАР
print("\n" + "="*50)
print("12-ЕСЕП: ПАРЛЫ ДИАГРАММАЛАР")
print("="*50)

# Алғашқы 5 сандық баған
алғашқы_5_сан = ['col_2', 'col_3', 'col_4', 'col_5', 'col_6']
sns.pairplot(df[алғашқы_5_сан + ['col_7']].sample(500), hue='col_7')
plt.show()

# 13-ЕСЕП: ТЕПЛОВАЯ КАРТА (ЖЫЛУ КАРТАСЫ)
print("\n" + "="*50)
print("13-ЕСЕП: КОРРЕЛЯЦИЯНЫҢ ЖЫЛУ КАРТАСЫ")
print("="*50)

plt.figure(figsize=(12, 10))
sns.heatmap(корреляция, annot=True, cmap='coolwarm', center=0, fmt='.2f')
plt.title('Сандық Бағандардың Корреляция Матрицасы', fontsize=14)
plt.show()

# 14-ЕСЕП: ӨҢДЕЛГЕН ДЕРЕКТЕРДІ САҚТАУ
print("\n" + "="*50)
print("14-ЕСЕП: EXCEL-ГЕ САҚТАУ")
print("="*50)

# Қажетті бағандар
сақталатын_бағандар = ['col_1', 'col_2', 'col_3', 'col_7', 'total_value', 'double_stock', 'log_price']
df_to_save = df[сақталатын_бағандар]

# Excel-ге сақтау
df_to_save.to_excel('catalog_analysis.xlsx', index=False)
print("Файл сақталды: catalog_analysis.xlsx")
print(f"Сақталған бағандар: {сақталатын_бағандар}")

# 15-ЕСЕП: ҚОРЫТЫНДЫ ЕСЕП
print("\n" + "="*50)
print("15-ЕСЕП: КАТЕГОРИЯ БОЙЫНША ҚОРЫТЫНДЫ")
print("="*50)

категория_қорытынды = df.groupby('col_7').agg(
    count=('col_1', 'count'),           # тауар саны
    mean_price=('col_2', 'mean'),       # орташа баға
    total_quantity=('col_3', 'sum'),    # жалпы саны
    mean_log_price=('log_price', 'mean') # орташа логарифм
).round(2)

print(категория_қорытынды)

# 16-ЕСЕП: ӘР КАТЕГОРИЯНЫҢ ЕҢ ҚЫМБАТЫ
print("\n" + "="*50)
print("16-ЕСЕП: ӘР КАТЕГОРИЯНЫҢ ЕҢ ҚЫМБАТ ТАУАРЫ")
print("="*50)

ең_қымбаттар = df.loc[df.groupby('col_7')['col_2'].idxmax()]
print(ең_қымбаттар[['col_1', 'col_2', 'col_7']])

# 17-ЕСЕП: ТОП-10 ЕҢ ҚҰНДЫ ТАУАР
print("\n" + "="*50)
print("17-ЕСЕП: ТОП-10 ЕҢ ҚҰНДЫ ТАУАР")
print("="*50)

топ_10_құнды = df.nlargest(10, 'total_value')[['col_1', 'col_2', 'col_3', 'total_value']]
print(топ_10_құнды)

# 18-ЕСЕП: БАҒА ДИАПАЗОНДАРЫ БОЙЫНША ТОПТАСТЫРУ
print("\n" + "="*50)
print("18-ЕСЕП: БАҒА ДИАПАЗОНДАРЫ")
print("="*50)

# Баға диапазондарын анықтау
def баға_диапазоны(баға):
    if баға <= 50:
        return '0-50'
    elif баға <= 200:
        return '50-200'
    elif баға <= 500:
        return '200-500'
    elif баға <= 1000:
        return '500-1000'
    else:
        return '>1000'

df['price_range'] = df['col_2'].apply(баға_диапазоны)

диапазон_стат = df.groupby('price_range').size().reset_index(name='count')
print(диапазон_стат)

# График
plt.figure(figsize=(10, 6))
sns.barplot(x='price_range', y='count', data=диапазон_стат, order=['0-50', '50-200', '200-500', '500-1000', '>1000'])
plt.title('Баға Диапазондары Бойынша Тауарлар Саны', fontsize=14)
plt.xlabel('Баға диапазоны (тг)', fontsize=12)
plt.ylabel('Тауарлар саны', fontsize=12)
plt.show()
# 19-ЕСЕП: ЕҢ ҚҰНДЫ КАТЕГОРИЯ
print("\n" + "="*50)
print("19-ЕСЕП: КАТЕГОРИЯЛАРДЫҢ ЖАЛПЫ ҚҰНЫ")
print("="*50)

категория_құн = df.groupby('col_7')['total_value'].sum().sort_values(ascending=False).reset_index()
print(категория_құн)

# График
plt.figure(figsize=(10, 6))
sns.barplot(x='total_value', y='col_7', data=категория_құн)
plt.title('Категориялардың Жалпы Құны', fontsize=14)
plt.xlabel('Жалпы құн (тг)', fontsize=12)
plt.ylabel('Категория', fontsize=12)
plt.show()


# 20-ЕСЕП: СЕБЕЛГЕН ДИАГРАММА
print("\n" + "="*50)
print("20-ЕСЕП: КАТЕГОРИЯ СЕБЕЛГЕН ДИАГРАММАСЫ")
print("="*50)

plt.figure(figsize=(8, 8))
категория_саны = df['col_7'].value_counts()
plt.pie(категория_саны, labels=категория_саны.index, autopct='%1.1f%%')
plt.title('Категориялардың Тауар Саны Бойынша Бөлінуі', fontsize=14)
plt.show()

# 21-ЕСЕП: КАТЕГОРИЯ БОЙЫНША ОРТАША БАҒА МЕН ҚОР
print("\n" + "="*50)
print("21-ЕСЕП: ОРТАША БАҒА МЕН ҚОР")
print("="*50)

категория_орт = df.groupby('col_7').agg(
    mean_price=('col_2', 'mean'),
    mean_stock=('col_3', 'mean')
).round(2)

print(категория_орт)

# График (scatter plot)
plt.figure(figsize=(10, 6))
for кат in категория_орт.index:
    plt.scatter(категория_орт.loc[кат, 'mean_price'],
                категория_орт.loc[кат, 'mean_stock'],
                s=200, label=кат)
plt.xlabel('Орташа баға (тг)')
plt.ylabel('Орташа қор саны')
plt.title('Категориялар: Орташа Баға vs Орташа Қор')
plt.legend()
plt.show()

# 22-ЕСЕП: БАҒА СТАНДАРТТЫ АУЫТҚУЫ

print("\n" + "="*50)
print("22-ЕСЕП: БАҒА СТАНДАРТТЫ АУЫТҚУЫ")
print("="*50)

категория_ауытқу = df.groupby('col_7')['col_2'].std().sort_values(ascending=False).reset_index()
print(категория_ауытқу)

# Горизонталь барплот
plt.figure(figsize=(10, 6))
sns.barplot(x='col_2', y='col_7', data=категория_ауытқу)
plt.title('Категориялар Бойынша Бағаның Ауытқуы', fontsize=14)
plt.xlabel('Стандартты ауытқу', fontsize=12)
plt.ylabel('Категория', fontsize=12)
plt.show()


# 23-ЕСЕП: НӨЛДІК ҚОРЫ БАР ТАУАРЛАР

print("\n" + "="*50)
print("23-ЕСЕП: НӨЛДІК ҚОРЫ БАР ТАУАРЛАР")
print("="*50)

нөлдік_қор = df[df['col_3'] == 0]
print(f"Нөлдік қоры бар тауарлар саны: {len(нөлдік_қор)}")
print(нөлдік_қор[['col_1', 'col_2', 'col_7']].head(10))


# 24-ЕСЕП: ТОП-5 КАТЕГОРИЯ
print("\n" + "="*50)
print("24-ЕСЕП: ТОП-5 КАТЕГОРИЯ")
print("="*50)

топ_5_категория = df['col_7'].value_counts().head(5).reset_index()
топ_5_категория.columns = ['category', 'count']
print(топ_5_категория)

plt.figure(figsize=(10, 6))
sns.barplot(x='count', y='category', data=топ_5_категория)
plt.title('Топ-5 Категория', fontsize=14)
plt.xlabel('Тауар саны', fontsize=12)
plt.ylabel('Категория', fontsize=12)
plt.show()

# 25-ЕСЕП: ТОП-10 ТАУАР (ҚОР БОЙЫНША)
print("\n" + "="*50)
print("25-ЕСЕП: ТОП-10 КӨП ҚОРЫ БАР ТАУАР")
print("="*50)

топ_10_қор = df.nlargest(10, 'col_3')[['col_1', 'col_3']]
print(топ_10_қор)

plt.figure(figsize=(10, 6))
sns.barplot(x='col_3', y='col_1', data=топ_10_қор)
plt.title('Топ-10 Көп Қоры Бар Тауар', fontsize=14)
plt.xlabel('Қор саны', fontsize=12)
plt.ylabel('Тауар аты', fontsize=12)
plt.show()

# 26-ЕСЕП: ПИВОТ КЕСТЕ (КАТЕГОРИЯ × ДИАПАЗОН)
print("\n" + "="*50)
print("26-ЕСЕП: ПИВОТ КЕСТЕ")
print("="*50)

пивот_кесте = pd.pivot_table(df,
                              index='col_7',
                              columns='price_range',
                              values='col_1',
                              aggfunc='count',
                              fill_value=0)

print(пивот_кесте)

# Heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(пивот_кесте, annot=True, cmap='YlOrRd', fmt='d')
plt.title('Категориялар мен Баға Диапазондарының Бөлінуі', fontsize=14)
plt.show()

# 27-ЕСЕП: БАҒА МЕН РЕЙТИНГ БАЙЛАНЫСЫ
print("\n" + "="*50)
print("27-ЕСЕП: БАҒА МЕН РЕЙТИНГ")
print("="*50)

plt.figure(figsize=(10, 6))
sns.regplot(x=df['col_2'], y=df['col_5'], scatter_kws={'alpha':0.3})
plt.title('Баға мен Рейтинг Байланысы', fontsize=14)
plt.xlabel('Баға (тг)', fontsize=12)
plt.ylabel('Рейтинг (1-5)', fontsize=12)
plt.show()

корреляция_баға_рейтинг = df['col_2'].corr(df['col_5'])
print(f"Баға мен рейтинг корреляциясы: {корреляция_баға_рейтинг:.3f}")

# 28-ЕСЕП: ЖОҒАРЫ РЕЙТИНГТІ ТАУАРЛАР
print("\n" + "="*50)
print("28-ЕСЕП: ЖОҒАРЫ РЕЙТИНГТІ ТАУАРЛАР")
print("="*50)

жоғары_рейтинг = df[df['col_5'] > 4.5]
print(f"Рейтингі 4.5-тен жоғары тауарлар саны: {len(жоғары_рейтинг)}")
print(жоғары_рейтинг[['col_1', 'col_2', 'col_5', 'col_7']].head(10))

# 29-ЕСЕП: ЖЕҢІЛДІК АНАЛИЗІ
print("\n" + "="*50)
print("29-ЕСЕП: ЖЕҢІЛДІК АНАЛИЗІ")
print("="*50)

# Жеңілдік бойынша топтастыру
df['discount_group'] = pd.cut(df['col_8'], bins=[0, 0.05, 0.1, 0.2, 0.3],
                               labels=['0-5%', '5-10%', '10-20%', '20-30%'])

жеңілдік_стат = df.groupby('discount_group').agg(
    count=('col_1', 'count'),
    mean_price=('col_2', 'mean'),
    mean_stock=('col_3', 'mean')
).round(2)

print(жеңілдік_стат)

# 30-ЕСЕП: АЙЛЫҚ САТЫЛЫМ АНАЛИЗІ
print("\n" + "="*50)
print("30-ЕСЕП: АЙЛЫҚ САТЫЛЫМ")
print("="*50)

айлық_сатылым = df.groupby('col_9')['col_6'].sum().reset_index()
print(айлық_сатылым)

plt.figure(figsize=(12, 6))
plt.plot(айлық_сатылым['col_9'], айлық_сатылым['col_6'], marker='o', linewidth=2)
plt.title('Айлар Бойынша Сатылым Динамакасы', fontsize=14)
plt.xlabel('Ай', fontsize=12)
plt.ylabel('Сатылым саны', fontsize=12)
plt.grid(True, alpha=0.3)
plt.xticks(range(1, 13))
plt.show()

# 31-ЕСЕП: СЕГМЕНТ АНАЛИЗІ
print("\n" + "="*50)
print("31-ЕСЕП: СЕГМЕНТ БОЙЫНША АНАЛИЗ")
print("="*50)

сегмент_стат = df.groupby('col_10').agg(
    count=('col_1', 'count'),
    mean_price=('col_2', 'mean'),
    mean_stock=('col_3', 'mean'),
    total_value=('total_value', 'sum')
).round(2)

print(сегмент_стат)

# 32-ЕСЕП: VIP ТАУАРЛАР
print("\n" + "="*50)
print("32-ЕСЕП: VIP ТАУАРЛАР (ҚҰНЫ > 10000)")
print("="*50)

vip_тауарлар = df[df['total_value'] > 10000]
print(f"VIP тауарлар саны: {len(vip_тауарлар)}")
print(vip_тауарлар[['col_1', 'col_2', 'col_3', 'total_value']].head(10))

# 33-ЕСЕП: КАТЕГОРИЯ БОЙЫНША ТОП-3 ТАУАР
print("\n" + "="*50)
print("33-ЕСЕП: ӘР КАТЕГОРИЯНЫҢ ТОП-3 ТАУАРЫ")
print("="*50)

def топ_3_тауар(категория_топ):
    return категория_топ.nlargest(3, 'total_value')[['col_1', 'total_value']]

әр_категория_топ3 = df.groupby('col_7').apply(топ_3_тауар)
print(әр_категория_топ3)

# 34-ЕСЕП: БАҒА МЕН САННЫҢ БАЙЛАНЫС МАТРИЦАСЫ
print("\n" + "="*50)
print("34-ЕСЕП: КАТЕГОРИЯЛАРДЫҢ БАЙЛАНЫСЫ")
print("="*50)

# Әр категориядағы баға мен санның корреляциясы
категория_корр = df.groupby('col_7').apply(
    lambda x: x['col_2'].corr(x['col_3'])
).round(3)

print(категория_корр)

# 35-ЕСЕП: ЭКСТРЕМАЛДЫ ТАУАРЛАР (3 сигма ережесі)
print("\n" + "="*50)
print("35-ЕСЕП: ЭКСТРЕМАЛДЫ ТАУАРЛАР")
print("="*50)

# Баға бойынша
орташа_баға = df['col_2'].mean()
сигма_баға = df['col_2'].std()
баға_экстремалды = df[abs(df['col_2'] - орташа_баға) > 3 * сигма_баға]