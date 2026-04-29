import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, confusion_matrix, \
    ConfusionMatrixDisplay
import warnings

warnings.filterwarnings('ignore')

plt.style.use('default')
sns.set_context("notebook", font_scale=1.1)

# =============================================================================
# ЗАДАЧА 1. Загрузка и изучение данных
# =============================================================================
print("Задача 1. Загрузка и первичный анализ данных")
df = pd.read_excel('catalog_products.xlsx')

print(f"Размер DataFrame: {df.shape}")
print("\nТипы данных:")
print(df.dtypes)
print("\nКоличество пропусков:")
print(df.isnull().sum())

print("\nКолонки, потенциально полезные для предсказания цены:")
print("- col_3: количество на складе")
print("- col_4, col_5, ...: технические/физические характеристики")
print("- col_7: категория товара")

# =============================================================================
# ЗАДАЧА 2. Очистка и преобразование данных
# =============================================================================
print("\nЗадача 2. Очистка данных")
num_cols = df.select_dtypes(include='number').columns
df[num_cols] = df[num_cols].astype(float)
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

text_cols = df.select_dtypes(include='object').columns
df = df.dropna(subset=text_cols).reset_index(drop=True)
print(f"Данные очищены. Итоговый размер: {df.shape}")

# =============================================================================
# ЗАДАЧА 3. Создание новых признаков
# =============================================================================
print("\nЗадача 3. Создание новых признаков")
df['total_value'] = df['col_2'] * df['col_3']
df['log_price'] = np.log1p(df['col_2'])
df['double_stock'] = df['col_3'] * 2
print("Созданы признаки: total_value, log_price, double_stock")

# =============================================================================
# ЗАДАЧА 4. Визуальный анализ данных
# =============================================================================
print("\nЗадача 4. Визуальный анализ")
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
sns.histplot(df['col_2'], bins=30, ax=axes[0], kde=True)
axes[0].set_title('Распределение цены (col_2)')

sns.scatterplot(data=df, x='col_3', y='col_2', alpha=0.5, ax=axes[1])
axes[1].set_title('Зависимость цены от количества (col_3)')

sns.boxplot(data=df, x='col_7', y='col_2', ax=axes[2])
axes[2].set_title('Распределение цены по категориям (col_7)')
axes[2].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.show()

# =============================================================================
# ЗАДАЧА 5. Выявление аномалий
# =============================================================================
print("\nЗадача 5. Выявление и удаление аномалий")
mean_price = df['col_2'].mean()
std_price = df['col_2'].std()

mask_anomaly = (df['col_2'] > mean_price + 3 * std_price) | \
               (df['col_2'] < mean_price - 3 * std_price)
anomalies = df[mask_anomaly].copy()
print(f"Выявлено аномальных записей: {len(anomalies)}")

df = df[~mask_anomaly].reset_index(drop=True)
print("Аномалии удалены из основного набора данных.")

# =============================================================================
# ЗАДАЧА 6. Кодирование категориальных признаков
# =============================================================================
print("\nЗадача 6. Кодирование категориальных признаков")
df['category_raw'] = df['col_7']
df_encoded = pd.get_dummies(df, columns=['col_7'], drop_first=True, prefix='cat')
print("Категориальная колонка преобразована. Оригинал сохранён в 'category_raw'.")
print(f"Количество колонок после кодирования: {df_encoded.shape[1]}")

# =============================================================================
# ЗАДАЧА 7. Разделение на признаки и целевую переменную
# =============================================================================
print("\nЗадача 7. Разделение выборки")
y = df_encoded['col_2']
X = df_encoded.drop(columns=['col_2'])
X = X.select_dtypes(include='number')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Обучающая выборка: {X_train.shape}, Тестовая выборка: {X_test.shape}")

# =============================================================================
# ЗАДАЧА 8. Простейшая линейная регрессия
# =============================================================================
print("\nЗадача 8. Базовая линейная регрессия")
lr_base = LinearRegression()
lr_base.fit(X_train, y_train)
y_pred_base = lr_base.predict(X_test)

mae_base = mean_absolute_error(y_test, y_pred_base)
mse_base = mean_squared_error(y_test, y_pred_base)
print(f"MAE (базовая модель): {mae_base:.2f}")
print(f"MSE (базовая модель): {mse_base:.2f}")

# =============================================================================
# ЗАДАЧА 9. Улучшение модели с использованием дополнительных признаков
# =============================================================================
print("\nЗадача 9. Модель с расширенным набором признаков")
features_extended = [c for c in X.columns if
                     c in ['col_3', 'total_value', 'double_stock', 'log_price'] or c.startswith('cat_')]
X_train_ext = X_train[features_extended]
X_test_ext = X_test[features_extended]

lr_ext = LinearRegression()
lr_ext.fit(X_train_ext, y_train)
y_pred_ext = lr_ext.predict(X_test_ext)

mae_ext = mean_absolute_error(y_test, y_pred_ext)
mse_ext = mean_squared_error(y_test, y_pred_ext)
print(f"MAE (расширенная модель): {mae_ext:.2f}")
print(f"MSE (расширенная модель): {mse_ext:.2f}")

# =============================================================================
# ЗАДАЧА 10. Визуализация предсказаний
# =============================================================================
print("\nЗадача 10. Визуализация предсказаний")
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred_ext, alpha=0.6, edgecolors='k', linewidth=0.5)
lims = [min(y_test.min(), y_pred_ext.min()), max(y_test.max(), y_pred_ext.max())]
plt.plot(lims, lims, 'r--', linewidth=2, label='y = x')
plt.xlabel('Истинная цена')
plt.ylabel('Предсказанная цена')
plt.title('Истинная vs Предсказанная цена')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

residuals = np.abs(y_test - y_pred_ext)
worst_idx = residuals.nlargest(5).index
print("Товары с наибольшей ошибкой предсказания:")
print(df_encoded.loc[worst_idx, ['col_2', 'col_3', 'category_raw']])

# =============================================================================
# ЗАДАЧА 11. Нормализация числовых признаков
# =============================================================================
print("\nЗадача 11. Нормализация признаков")
scaler = StandardScaler()
num_features_to_scale = ['col_3', 'total_value', 'double_stock', 'log_price']
num_features_to_scale = [c for c in num_features_to_scale if c in X.columns]

X_train_scaled = X_train.copy()
X_test_scaled = X_test.copy()
X_train_scaled[num_features_to_scale] = scaler.fit_transform(X_train[num_features_to_scale])
X_test_scaled[num_features_to_scale] = scaler.transform(X_test[num_features_to_scale])

print("Данные масштабированы с использованием StandardScaler.")
print("Проверка масштаба (среднее ~0):")
print(X_train_scaled[num_features_to_scale].mean())

# =============================================================================
# ЗАДАЧА 12. Feature Importance (важность признаков)
# =============================================================================
print("\nЗадача 12. Важность признаков")
dt_model = DecisionTreeRegressor(random_state=42)
dt_model.fit(X_train_scaled, y_train)

importances = dt_model.feature_importances_
feat_names = X_train_scaled.columns
importance_df = pd.DataFrame({'feature': feat_names, 'importance': importances})
importance_df = importance_df.sort_values('importance', ascending=False).head(10)

plt.figure(figsize=(8, 5))
sns.barplot(data=importance_df, x='importance', y='feature', palette='viridis')
plt.title('Важность признаков (DecisionTreeRegressor)')
plt.xlabel('Важность')
plt.ylabel('Признак')
plt.tight_layout()
plt.show()

# =============================================================================
# ЗАДАЧА 13. Использование полиномиальных признаков
# =============================================================================
print("\nЗадача 13. Полиномиальные признаки (degree=2)")
poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train_scaled[num_features_to_scale])
X_test_poly = poly.transform(X_test_scaled[num_features_to_scale])

lr_poly = LinearRegression()
lr_poly.fit(X_train_poly, y_train)
y_pred_poly = lr_poly.predict(X_test_poly)

mae_poly = mean_absolute_error(y_test, y_pred_poly)
mse_poly = mean_squared_error(y_test, y_pred_poly)
print(f"MAE (полиномиальная модель): {mae_poly:.2f}")
print(f"MSE (полиномиальная модель): {mse_poly:.2f}")

# =============================================================================
# ЗАДАЧА 14. KNN для предсказания цены
# =============================================================================
print("\nЗадача 14. KNeighborsRegressor (k=5)")
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train_scaled, y_train)
y_pred_knn = knn.predict(X_test_scaled)

mae_knn = mean_absolute_error(y_test, y_pred_knn)
mse_knn = mean_squared_error(y_test, y_pred_knn)
print(f"MAE (KNN): {mae_knn:.2f}")
print(f"MSE (KNN): {mse_knn:.2f}")

print("\nСравнение моделей:")
models_res = pd.DataFrame({
    'Model': ['Linear Base', 'Linear Extended', 'Polynomial', 'KNN'],
    'MAE': [mae_base, mae_ext, mae_poly, mae_knn],
    'MSE': [mse_base, mse_ext, mse_poly, mse_knn]
})
print(models_res)

# =============================================================================
# ЗАДАЧА 15. Разделение данных по категориям
# =============================================================================
print("\nЗадача 15. Отдельные модели по категориям")
category_metrics = []
for cat_val in df_encoded['category_raw'].dropna().unique():
    subset = df_encoded[df_encoded['category_raw'] == cat_val]
    if len(subset) < 10:
        continue
    y_cat = subset['col_2']
    X_cat = subset.drop(columns=['col_2']).select_dtypes(include='number')

    X_tr, X_te, y_tr, y_te = train_test_split(X_cat, y_cat, test_size=0.2, random_state=42)
    lr_cat = LinearRegression()
    lr_cat.fit(X_tr, y_tr)
    y_pred_cat = lr_cat.predict(X_te)

    mae_cat = mean_absolute_error(y_te, y_pred_cat)
    category_metrics.append({'category': cat_val, 'MAE': mae_cat})

cat_metrics_df = pd.DataFrame(category_metrics)
print("Метрики по категориям:")
print(cat_metrics_df.sort_values('MAE'))

# =============================================================================
# ЗАДАЧА 16. Визуализация предсказаний по категориям
# =============================================================================
print("\nЗадача 16. Визуализация по категориям")
n_cats = min(len(cat_metrics_df), 6)
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, row in enumerate(cat_metrics_df.head(n_cats).iterrows()):
    idx, cat_data = row
    cat_name = cat_data['category']
    subset = df_encoded[df_encoded['category_raw'] == cat_name]
    y_true = subset['col_2']
    X_sub = subset.drop(columns=['col_2']).select_dtypes(include='number')

    X_tr, X_te, y_tr, y_te = train_test_split(X_sub, y_true, test_size=0.2, random_state=42)
    lr_vis = LinearRegression()
    lr_vis.fit(X_tr, y_tr)
    y_pr = lr_vis.predict(X_te)

    axes[i].scatter(y_te, y_pr, alpha=0.7, edgecolor='k')
    lims = [min(y_te.min(), y_pr.min()), max(y_te.max(), y_pr.max())]
    axes[i].plot(lims, lims, 'r--')
    axes[i].set_title(f'Категория: {cat_name}')
    axes[i].set_xlabel('Истинная')
    axes[i].set_ylabel('Предсказанная')

for j in range(i + 1, len(axes)):
    axes[j].axis('off')
plt.tight_layout()
plt.show()

# =============================================================================
# ЗАДАЧА 17. Кросс-валидация
# =============================================================================
print("\nЗадача 17. Кросс-валидация (5 фолдов)")
cv_mae = cross_val_score(LinearRegression(), X_train_scaled, y_train, cv=5, scoring='neg_mean_absolute_error')
cv_mse = cross_val_score(LinearRegression(), X_train_scaled, y_train, cv=5, scoring='neg_mean_squared_error')

print(f"Среднее MAE (CV): {-cv_mae.mean():.2f} ± {cv_mae.std():.2f}")
print(f"Среднее MSE (CV): {-cv_mse.mean():.2f} ± {cv_mse.std():.2f}")

# =============================================================================
# ЗАДАЧА 18. Простейшая классификация (категория цен)
# =============================================================================
print("\nЗадача 18. Классификация по ценовым диапазонам")
bins = [0, 100, 500, np.inf]
labels = [0, 1, 2]
df_encoded['price_class'] = pd.cut(df_encoded['col_2'], bins=bins, labels=labels, right=False)

y_cls = df_encoded['price_class']
X_cls = df_encoded.drop(columns=['col_2', 'price_class']).select_dtypes(include='number')

X_tr_cls, X_te_cls, y_tr_cls, y_te_cls = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42)
dt_cls = DecisionTreeClassifier(random_state=42, max_depth=5)
dt_cls.fit(X_tr_cls, y_tr_cls)
y_pred_cls = dt_cls.predict(X_te_cls)

acc = accuracy_score(y_te_cls, y_pred_cls)
print(f"Точность классификации (Accuracy): {acc:.4f}")

# =============================================================================
# ЗАДАЧА 19. Confusion Matrix и визуализация классификации
# =============================================================================
print("\nЗадача 19. Матрица ошибок")
cm = confusion_matrix(y_te_cls, y_pred_cls, labels=[0, 1, 2])
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Низкая (0)', 'Средняя (1)', 'Высокая (2)'])
disp.plot(cmap='Blues', values_format='d')
plt.title('Confusion Matrix: Классификация цен')
plt.grid(False)
plt.show()

# =============================================================================
# ЗАДАЧА 20. Финальная модель и сохранение результатов (ИСПРАВЛЕНО)
# =============================================================================
print("\nЗадача 20. Сохранение результатов и формирование отчёта")
df_encoded['predicted_price'] = np.nan
df_encoded['predicted_class'] = np.nan

# Регрессия: предсказываем ТОЛЬКО на тех признаках, на которых обучали lr_ext
df_encoded.loc[X_test_ext.index, 'predicted_price'] = lr_ext.predict(X_test_ext)

# Классификация: предсказываем на полном наборе признаков
df_encoded.loc[X_cls.index, 'predicted_class'] = dt_cls.predict(X_cls)

df_encoded.to_excel('catalog_ml_predictions.xlsx', index=False)
print("Результаты сохранены в файл catalog_ml_predictions.xlsx")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

axes[0].scatter(y_test, y_pred_ext, alpha=0.6, edgecolor='k')
lims = [min(y_test.min(), y_pred_ext.min()), max(y_test.max(), y_pred_ext.max())]
axes[0].plot(lims, lims, 'r--')
axes[0].set_title('Предсказанная vs Истинная цена')
axes[0].set_xlabel('Истинная')
axes[0].set_ylabel('Предсказанная')

axes[1].barh(importance_df['feature'].values, importance_df['importance'].values, color='teal')
axes[1].set_title('Важность признаков')
axes[1].invert_yaxis()

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[2],
            xticklabels=['Низкая', 'Средняя', 'Высокая'],
            yticklabels=['Низкая', 'Средняя', 'Высокая'])
axes[2].set_title('Confusion Matrix')
axes[2].set_xlabel('Предсказанный класс')
axes[2].set_ylabel('Истинный класс')

plt.tight_layout()
plt.savefig('ml_report_summary.png', dpi=300)
plt.show()
print("Визуальный отчёт сохранён как ml_report_summary.png")
print("Проект завершён успешно.")