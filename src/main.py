class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products) if self.products else 0}"

    def __repr__(self):
        return f"Category(name={self.name!r}, products_count={len(self.products) if self.products else 0})"

    def add_product(self, product):
        """Добавляет продукт в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
        else:
            raise ValueError("Можно добавлять только объекты класса Product")


    @property
    def products_info(self):
        """Свойство, возвращающее информацию о продуктах"""
        if not self.__products:
            return f"В категории '{self.name}' нет продуктов"

        result = f"Категория: {self.name}\n"
        for product in self.__products:
            result += f"  - {product}\n"
        return result


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

    # # Создаем продукты
    # apple = Product("Яблоки", 100, 50)
    # banana = Product("Бананы", 80, 30)
    #
    # # Создаем категорию
    # fruits = Category("Фрукты")
    #
    # # Добавляем продукты
    # fruits.add_product(apple)
    # fruits.add_product(banana)
    #
    # # Выводим информацию
    # print(fruits.products_info)
    #
    # # Добавляем еще один продукт
    # orange = Product("Апельсины", 120, 20)
    # fruits.add_product(orange)
    #
    # # Снова выводим (информация обновилась)
    # print("\nПосле добавления апельсинов:")
    # print(fruits.products_info)
