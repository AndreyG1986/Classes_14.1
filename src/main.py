class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __add__(self, other):
        """
        Метод срабатывает, когда используется оператор сложения.
        В параметре other хранится то, что справа от знака +
        """
        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self):
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер для цены с проверкой"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, prod_data):
        """Создает новый продукт из словаря с данными"""
        # Проверяем, что prod_data является словарем
        if not isinstance(prod_data, dict):
            raise TypeError("Данные должны быть представлены в виде словаря")

        # Извлекаем данные из словаря
        name = prod_data.get("name")
        description = prod_data.get("description")
        price = prod_data.get("price")
        quantity = prod_data.get("quantity")

        # Создаем и возвращаем новый объект Product
        return cls(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"


class Category:
    name: str
    description: str
    product_count: int = 0  # Количество уникальных позиций продуктов
    category_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []  # Приватный список продуктов
        Category.category_count += 1

        # Добавляем продукты при создании категории
        for product in products:
            self.add_product(product)

    def __str__(self):
        """
        Возвращает название категории и общее количество товаров на складе.
        Общее количество рассчитывается как сумма quantity всех продуктов.
        """
        total_quantity = self.get_total_quantity()
        return f"{self.name}, количество товаров: {total_quantity} шт."

    def __repr__(self):
        total_quantity = self.get_total_quantity()
        return f"Category(name={self.name!r}, total_products={total_quantity})"

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1  # Увеличиваем счетчик уникальных позиций
        else:
            raise ValueError("Можно добавлять только объекты класса Product")

    def get_total_quantity(self):
        """
        Вычисляет общее количество товаров на складе,
        суммируя quantity всех продуктов в категории
        """
        total = 0
        for product in self.__products:
            total += product.quantity
        return total

    @property
    def products(self):
        """Геттер для атрибута products - возвращает строку с информацией о продуктах"""
        if not self.__products:
            return f"В категории '{self.name}' нет продуктов"

        result = ""
        for product in self.__products:
            # Используем формат из __str__ метода Product
            result += f"{product}\n"
        return result.rstrip()  # Убираем лишний перенос строки в конце

    @property
    def products_info(self):
        """Свойство, возвращающее информацию о продуктах"""
        if not self.__products:
            return f"В категории '{self.name}' нет продуктов"

        result = f"Категория: {self.name}\n"
        for product in self.__products:
            result += f"  - {product}\n"
        return result.rstrip()  # Убираем лишний перенос строки

    # Если нужен доступ к списку продуктов как к объектам
    def get_products_list(self):
        """Возвращает список объектов продуктов"""
        return self.__products.copy()  # Возвращаем копию для безопасности


if __name__ == "__main__":
    print("\n=== Задание 15.1 магические методы ===")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
