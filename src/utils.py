class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Category:
    def __init__(self, name):
        self.name = name
        self.__products = []

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


# Использование
if __name__ == "__main__":
    # Создаем продукты
    apple = Product("Яблоки", 100, 50)
    banana = Product("Бананы", 80, 30)

    # Создаем категорию
    fruits = Category("Фрукты")

    # Добавляем продукты
    fruits.add_product(apple)
    fruits.add_product(banana)

    # Выводим информацию
    print(fruits.products_info)

    # Добавляем еще один продукт
    orange = Product("Апельсины", 120, 20)
    fruits.add_product(orange)

    # Снова выводим (информация обновилась)
    print("\nПосле добавления апельсинов:")
    print(fruits.products_info)