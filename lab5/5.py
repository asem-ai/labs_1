import numpy as np
import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional
import warnings

warnings.filterwarnings('ignore')


# ======================== БЛОК 1. Вводные данные и базовая обработка ========================

# Задача 1 — Класс User
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self._id = user_id
        # name: Title Case + удаление пробелов
        self._name = name.strip().title()
        # email: lower()
        self._email = email.lower()
        # Проверка наличия @
        if '@' not in self._email:
            raise ValueError("Email must contain '@'")

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    def __str__(self):
        return f"User(id={self._id}, name='{self._name}', email='{self._email}')"

    def __del__(self):
        print(f"User {self._name} deleted")

    # Задача 2 — Фабричный метод from_string
    @classmethod
    def from_string(cls, data: str):
        parts = [part.strip() for part in data.split(',')]
        if len(parts) != 3:
            raise ValueError("Invalid format. Expected: id,name,email")
        user_id = int(parts[0])
        name = parts[1]
        email = parts[2]
        return cls(user_id, name, email)


# Задача 3 — Класс Product
class Product:
    def __init__(self, product_id: int, name: str, price: float, category: str):
        self.id = product_id
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', price={self.price}, category='{self.category}')"

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.id == other.id
        return False

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category
        }


# Задача 4 — Класс Inventory
class Inventory:
    def __init__(self):
        self._products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        self._products[product.id] = product

    def remove_product(self, product_id: int):
        if product_id in self._products:
            del self._products[product_id]

    def get_product(self, product_id: int) -> Optional[Product]:
        return self._products.get(product_id)

    def get_all_products(self) -> List[Product]:
        return list(self._products.values())

    def unique_products(self) -> set:
        return set(self._products.values())

    def to_dict(self) -> dict:
        return self._products.copy()

    # Задача 5 — Фильтрация продуктов (Lambda + Comprehension)
    def filter_by_price(self, min_price: float) -> List[Product]:
        return [p for p in self._products.values() if (lambda x: x.price >= min_price)(p)]


# Задача 6 — Logger действий (Файлы)
class Logger:
    @staticmethod
    def log_action(user: User, action: str, product: Product, filename: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(f"{timestamp};{user.id};{action};{product.id}\n")

    @staticmethod
    def read_logs(filename: str) -> List[dict]:
        logs = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(';')
                    if len(parts) == 4:
                        logs.append({
                            'timestamp': parts[0],
                            'user_id': int(parts[1]),
                            'action': parts[2],
                            'product_id': int(parts[3])
                        })
        except FileNotFoundError:
            pass
        return logs


# Задача 7 — Класс Order
class Order:
    def __init__(self, order_id: int, user: User, products: List[Product] = None):
        self.id = order_id
        self.user = user
        self.products = products if products is not None else []

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product_id: int):
        self.products = [p for p in self.products if p.id != product_id]

    def total_price(self) -> float:
        return sum(p.price for p in self.products)

    def __str__(self):
        product_names = ', '.join(p.name for p in self.products)
        return f"Order(id={self.id}, user='{self.user.name}', products=[{product_names}], total={self.total_price()})"

    # Задача 8 — Самые дорогие продукты
    def most_expensive_products(self, n: int) -> List[Product]:
        return sorted(self.products, key=lambda p: p.price, reverse=True)[:n]


# Задача 9 — Генератор цен
def price_stream(products: List[Product]):
    for product in products:
        yield product.price


# Задача 10 — Итератор по заказам
class OrderIterator:
    def __init__(self, orders: List[Order]):
        self.orders = orders
        self._index = 0

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.orders):
            result = self.orders[self._index]
            self._index += 1
            return result
        raise StopIteration


# ======================== БЛОК 2. Основы Numpy ========================

import numpy as np


# Задача 11 — Создание массива цен
def create_price_array(products: List[Product]) -> np.ndarray:
    return np.array([p.price for p in products], dtype=float)


# Задача 12 — Средняя и медианная цена
def mean_median_price(prices: np.ndarray) -> tuple:
    return (np.mean(prices), np.median(prices))


# Задача 13 — Нормализация цен
def normalize_prices(prices: np.ndarray) -> np.ndarray:
    min_price = np.min(prices)
    max_price = np.max(prices)
    if max_price == min_price:
        return np.zeros_like(prices)
    return (prices - min_price) / (max_price - min_price)


# Задача 14 — Массив категорий
def create_category_array(products: List[Product]) -> np.ndarray:
    return np.array([p.category for p in products])


# Задача 15 — Уникальные категории
def unique_categories_count(categories: np.ndarray) -> int:
    return len(np.unique(categories))


# Задача 16 — Продукты дороже среднего
def products_above_mean(products: List[Product], prices: np.ndarray) -> List[Product]:
    mean_price = np.mean(prices)
    return [p for p, price in zip(products, prices) if price > mean_price]


# Задача 17 — Векторная скидка
def apply_discount(prices: np.ndarray, discount: float = 0.1) -> np.ndarray:
    return prices * (1 - discount)


# Задача 18 — Массив заказов пользователей
def create_orders_matrix(orders: List[Order]) -> np.ndarray:
    return np.array([[order.total_price()] for order in orders])


# Задача 19 — Средняя покупка на пользователя
def avg_order_per_user(orders_array: np.ndarray) -> float:
    return np.mean(orders_array)


# Задача 20 — Индексы заказов дороже 1000
def expensive_order_indices(orders_array: np.ndarray, threshold: float = 1000) -> List[int]:
    return np.where(orders_array.flatten() > threshold)[0].tolist()


# ======================== БЛОК 3. Pandas ========================

import pandas as pd


# Задача 21 — DataFrame пользователей
def create_users_df(users: List[User]) -> pd.DataFrame:
    data = {
        'id': [u.id for u in users],
        'name': [u.name for u in users],
        'email': [u.email for u in users],
        'registration_date': [datetime.now().strftime("%Y-%m-%d") for _ in users]
    }
    return pd.DataFrame(data)


# Задача 22 — DataFrame продуктов
def create_products_df(products: List[Product]) -> pd.DataFrame:
    data = {
        'id': [p.id for p in products],
        'name': [p.name for p in products],
        'category': [p.category for p in products],
        'price': [p.price for p in products]
    }
    return pd.DataFrame(data)


# Задача 23 — Объединение пользователей и заказов
def merge_users_orders(users_df: pd.DataFrame, orders_df: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(orders_df, users_df[['id', 'name']], left_on='user_id', right_on='id', how='inner')[
        ['order_id', 'name', 'total']].rename(columns={'name': 'user_name'})


# Задача 24 — Фильтрация заказов по сумме
def filter_orders_by_total(orders_df: pd.DataFrame, min_total: float) -> pd.DataFrame:
    return orders_df[orders_df['total'] > min_total]


# Задача 25 — Группировка заказов по пользователю (сумма)
def group_orders_sum(orders_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.groupby('user_name')['total'].sum().reset_index().rename(columns={'total': 'total_sum'})


# Задача 26 — Средний заказ по пользователям
def group_orders_mean(orders_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.groupby('user_name')['total'].mean().reset_index().rename(columns={'total': 'mean_total'})


# Задача 27 — Количество заказов на пользователя
def orders_count_per_user(orders_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.groupby('user_name').size().reset_index(name='orders_count')


# Задача 28 — Средняя цена продукта по категориям
def mean_price_by_category(products_df: pd.DataFrame) -> pd.DataFrame:
    return products_df.groupby('category')['price'].mean().reset_index().rename(columns={'price': 'mean_price'})


# Задача 29 — Добавление столбца со скидкой
def add_discount_column(products_df: pd.DataFrame, discount: float = 0.1) -> pd.DataFrame:
    df = products_df.copy()
    df['discounted_price'] = df['price'] * (1 - discount)
    return df


# Задача 30 — Сортировка продуктов по цене
def sort_products_by_price(products_df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
    return products_df.sort_values('price', ascending=ascending).reset_index(drop=True)


# Задача 31 — Добавление колонки quantity
def add_quantity_column(orders_df: pd.DataFrame) -> pd.DataFrame:
    df = orders_df.copy()
    df['quantity'] = 1
    return df


# Задача 32 — Суммарная стоимость заказа
def add_total_price_column(orders_df: pd.DataFrame) -> pd.DataFrame:
    df = orders_df.copy()
    if 'quantity' not in df.columns:
        df['quantity'] = 1
    df['total_price'] = df['price'] * df['quantity']
    return df


# Задача 33 — Фильтрация по категории
def filter_by_category(products_df: pd.DataFrame, category: str) -> pd.DataFrame:
    return products_df[products_df['category'] == category]


# Задача 34 — Количество продуктов в каждой категории
def count_products_by_category(products_df: pd.DataFrame) -> pd.DataFrame:
    return products_df.groupby('category').size().reset_index(name='count')


# Задача 35 — Средняя цена по категориям
def mean_price_by_category_pd(products_df: pd.DataFrame) -> pd.DataFrame:
    return products_df.groupby('category')['price'].mean().reset_index(name='mean_price')


# Задача 36 — Сортировка заказов по total_price
def sort_orders_by_total(orders_df: pd.DataFrame, ascending: bool = False) -> pd.DataFrame:
    return orders_df.sort_values('total_price', ascending=ascending).reset_index(drop=True)


# Задача 37 — Топ-N самых дорогих заказов
def top_n_expensive_orders(orders_df: pd.DataFrame, n: int) -> pd.DataFrame:
    return orders_df.nlargest(n, 'total_price').reset_index(drop=True)


# Задача 38 — Объединение заказов и пользователей
def merge_orders_users(orders_df: pd.DataFrame, users_df: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(orders_df, users_df, left_on='user_id', right_on='id', how='inner')[
        ['order_id', 'name', 'total_price']].rename(columns={'name': 'user_name'})


# Задача 39 — Средняя сумма заказа на пользователя
def mean_order_per_user(orders_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.groupby('user_name')['total_price'].mean().reset_index(name='mean_total')


# Задача 40 — Количество заказов на пользователя
def count_orders_per_user(orders_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.groupby('user_name').size().reset_index(name='orders_count')


# Задача 41 — Максимальная цена заказа на пользователя
def max_order_per_user(orders_df: pd.DataFrame) -> pd.DataFrame:
    return orders_df.groupby('user_name')['total_price'].max().reset_index(name='max_order')


# Задача 42 — Количество уникальных категорий на пользователя
def unique_categories_per_user(orders_with_categories: pd.DataFrame) -> pd.DataFrame:
    return orders_with_categories.groupby('user_name')['category'].nunique().reset_index(name='unique_categories')


# Задача 43 — Добавление столбца VIP
def add_vip_column(users_summary: pd.DataFrame, threshold: float = 1000) -> pd.DataFrame:
    df = users_summary.copy()
    df['VIP'] = df['total_sum'] > threshold
    return df


# Задача 44 — Сортировка пользователей по total_sum и mean_total
def sort_users_complex(users_df: pd.DataFrame) -> pd.DataFrame:
    return users_df.sort_values(['total_sum', 'mean_total'], ascending=[False, True]).reset_index(drop=True)


# Задача 45 — Финальный агрегированный отчет
def create_final_report(orders_with_details: pd.DataFrame) -> pd.DataFrame:
    report = orders_with_details.groupby('user_name').agg(
        total_orders=('order_id', 'count'),
        total_sum=('total_price', 'sum'),
        mean_total=('total_price', 'mean'),
        max_order=('total_price', 'max'),
        unique_categories=('category', 'nunique')
    ).reset_index()
    report['VIP'] = report['total_sum'] > 1000
    return report


# ======================== Пример использования ========================

if __name__ == "__main__":
    # Демонстрация работы основных классов
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ РЕШЕНИЙ")
    print("=" * 60)

    # Создание пользователей
    u1 = User(1, " john doe ", "John@Example.COM")
    u2 = User.from_string("2, Alice Wonderland , alice@wonder.com")
    print("Пользователи созданы:")
    print(u1)
    print(u2)

    # Создание продуктов
    p1 = Product(1, "Laptop", 1200.0, "Electronics")
    p2 = Product(2, "Mouse", 25.0, "Electronics")
    p3 = Product(3, "T-Shirt", 20.0, "Clothing")
    p4 = Product(4, "Monitor", 450.0, "Electronics")

    # Инвентарь
    inv = Inventory()
    for p in [p1, p2, p3, p4]:
        inv.add_product(p)

    # Фильтрация по цене
    expensive_products = inv.filter_by_price(100.0)
    print(f"\nПродукты дороже 100: {[p.name for p in expensive_products]}")

    # Создание заказов
    order1 = Order(101, u1, [p1])
    order2 = Order(102, u2, [p2, p1])
    order3 = Order(103, u1, [p3, p4])

    print(f"\nЗаказ 1: {order1}")
    print(f"Общая стоимость заказа 2: {order2.total_price()}")
    print(f"3 самых дорогих продукта в заказе 2: {[p.name for p in order2.most_expensive_products(3)]}")

    # Numpy демонстрация
    products_list = [p1, p2, p4]
    prices = create_price_array(products_list)
    print(f"\nМассив цен: {prices}")
    mean_price, median_price = mean_median_price(prices)
    print(f"Средняя цена: {mean_price:.2f}, Медианная: {median_price}")
    print(f"Нормализованные цены: {normalize_prices(prices)}")

    # Pandas демонстрация
    users_df = create_users_df([u1, u2])
    print("\nDataFrame пользователей:")
    print(users_df)

    products_df = create_products_df([p1, p2, p3, p4])
    print("\nDataFrame продуктов:")
    print(products_df)

    orders_data = pd.DataFrame([
        {'order_id': 101, 'user_id': 1, 'total': 1200},
        {'order_id': 102, 'user_id': 2, 'total': 1225},
        {'order_id': 103, 'user_id': 1, 'total': 470}
    ])

    merged = merge_users_orders(users_df, orders_data)
    print("\nОбъединенные заказы с пользователями:")
    print(merged)

    print("\n" + "=" * 60)
    print("Все задачи успешно реализованы!")
    print("=" * 60)