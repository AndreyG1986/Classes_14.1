import pytest
from src.base_classes import Product, Category


@pytest.fixture()
def product_1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture()
def product_3():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture()
def product_4():
    return Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)


@pytest.fixture
def category_1(product_1, product_2, product_3):
    """Фикстура для категории с тремя продуктами"""
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product_1, product_2, product_3],
    )
    # Убираем явные add_product, так как они уже добавляются в конструкторе
    return category


@pytest.fixture
def category_2(product_4):
    """Фикстура для категории с одним продуктом"""
    category = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product_4],
    )
    # Убираем явные add_product, так как они уже добавляются в конструкторе
    return category


@pytest.fixture
def empty_category():
    """Фикстура для пустой категории"""
    return Category("Пустая категория", "Без продуктов", [])


@pytest.fixture(autouse=True)
def reset_counters_before_test():
    """Фикстура для сброса счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
