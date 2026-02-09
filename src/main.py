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
    products: list
    product_count: int = 0
    category_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

        # ВАЖНО: добавляем продукты при создании категории
        for product in products:
            self.add_product(product)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products) if self.products else 0}"

    def __repr__(self):
        return f"Category(name={self.name!r}, products_count={len(self.products) if self.products else 0})"

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1  # Увеличиваем счетчик продуктов
        else:
            raise ValueError("Можно добавлять только объекты класса Product")


    @property
    def products(self):
        """Геттер для атрибута products - возвращает строку с информацией о продуктах"""
        if not self.__products:
            return f"В категории '{self.name}' нет продуктов"

        result = ""
        for product in self.__products:
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
    # Создаем продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    # print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    # print(len(category2.products))
    # print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # Добавляем продукты
    category1.add_product(product1)
    category1.add_product(product2)
    category1.add_product(product3)
    category2.add_product(product4)

    # Выводим информацию
    print(category1.products_info)
    print(category2.products_info)

    # Создаем новый продукт через класс-метод, используя словарь, как в задании
    # "принимать на вход параметры товара в словаре и возвращать созданный объект класса Product"

    new_product_data = {
        "name": "Телефон Nokia 3310",
        "description": "Легендарный надежный телефон",
        "price": 5000.0,
        "quantity": 20,
    }

    new_prod_1 = Product.new_product(new_product_data)
    print(new_prod_1)  # Телефон Nokia 3310, 5000.0 руб. Остаток: 20 шт.
    print(type(new_prod_1))  # <class '__main__.Product'>
