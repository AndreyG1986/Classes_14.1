import pytest


class TestMainExceptions:
    """Тесты для обработки исключений в main.py - только базовые проверки"""

    def test_product_with_zero_quantity_raises_exception(self):
        """Тест проверяет, что при создании продукта с нулевым количеством возникает исключение"""
        from src.base_classes import Product

        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Product("Бракованный товар", "Неверное количество", 1000.0, 0)


class TestMainRefactored:
    """Тесты для функций из main.py (если вы вынесете логику в функции)"""

    def test_create_product_function(self):
        """Тест создания продукта"""
        from src.base_classes import Product

        # Создаем продукт напрямую
        product = Product("Test", "Desc", 100, 5)

        assert product.name == "Test"
        assert product.description == "Desc"
        assert product.price == 100
        assert product.quantity == 5

    def test_calculate_middle_price_function(self):
        """Тест расчета средней цены"""
        from src.base_classes import Product, Category

        products = [
            Product("P1", "D1", 100, 2),
            Product("P2", "D2", 200, 3)
        ]
        category = Category("Test", "Desc", products)

        # Средняя цена = (100 + 200) / 2 = 150
        assert category.middle_price() == 150.0

    def test_calculate_middle_price_empty_category(self):
        """Тест расчета средней цены в пустой категории"""
        from src.base_classes import Category

        category = Category("Empty", "Desc", [])

        # Для пустой категории должна вернуться 0
        assert category.middle_price() == 0


# Параметризованные тесты для различных сценариев создания продуктов
@pytest.mark.parametrize("name,desc,price,quantity", [
    ("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5),
    ("Iphone 15", "512GB", 210000.0, 8),
    ("Xiaomi Redmi Note 11", "1024GB", 31000.0, 14),
])
def test_product_creation_scenarios(name, desc, price, quantity):
    """Параметризованный тест для разных сценариев создания продуктов"""
    from src.base_classes import Product

    product = Product(name, desc, price, quantity)
    assert product.name == name
    assert product.description == desc
    assert product.price == price
    assert product.quantity == quantity


# Тест для проверки создания категории с продуктами
def test_category_creation():
    """Тест создания категории с продуктами"""
    from src.base_classes import Product, Category

    products = [
        Product("Product 1", "Description 1", 100.0, 5),
        Product("Product 2", "Description 2", 200.0, 10),
    ]

    category = Category("Test Category", "Test Description", products)

    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.get_total_quantity() == 15  # 5 + 10


# Тест для проверки строкового представления продукта
def test_product_str_repr():
    """Тест строкового представления продукта"""
    from src.base_classes import Product

    product = Product("Test Product", "Test Description", 150.0, 7)

    assert str(product) == "Test Product, 150.0 руб. Остаток: 7 шт."
    assert repr(product) == "Product(name='Test Product', price=150.0, quantity=7)"


# Тест для проверки геттера и сеттера цены
def test_product_price_setter():
    """Тест установки цены продукта"""
    from src.base_classes import Product

    product = Product("Test Product", "Test Description", 150.0, 7)

    # Проверяем геттер
    assert product.price == 150.0

    # Устанавливаем новую цену
    product.price = 200.0
    assert product.price == 200.0

    # Пытаемся установить отрицательную цену (не должна измениться)
    product.price = -50
    assert product.price == 200.0


# Тест для проверки метода __add__
def test_product_addition():
    """Тест сложения продуктов"""
    from src.base_classes import Product

    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)

    # Сумма стоимости = (100 * 5) + (200 * 3) = 500 + 600 = 1100
    assert product1 + product2 == 1100.0


# Тест для проверки создания продукта через класс-метод new_product
def test_new_product_creation():
    """Тест создания продукта через класс-метод"""
    from src.base_classes import Product

    product_data = {
        "name": "New Product",
        "description": "New Description",
        "price": 300.0,
        "quantity": 10
    }

    product = Product.new_product(product_data)

    assert product.name == "New Product"
    assert product.description == "New Description"
    assert product.price == 300.0
    assert product.quantity == 10