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