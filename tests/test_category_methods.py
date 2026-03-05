import pytest
from src.base_classes import Category, Product


class TestCategoryAddProduct:
    """Тесты для метода add_product"""

    def test_add_product_to_category(self, category_1, product_4):
        """Тест добавления продукта в категорию"""
        initial_product_count = Category.product_count
        initial_category_products = len(category_1.get_products_list())

        category_1.add_product(product_4)

        assert len(category_1.get_products_list()) == initial_category_products + 1
        assert Category.product_count == initial_product_count + 1
        assert product_4 in category_1.get_products_list()

    def test_add_invalid_product_type(self, category_1):
        """Тест добавления объекта неправильного типа"""
        with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product"):
            category_1.add_product("not a product")

    def test_add_same_product_multiple_times(self, category_1, product_1):
        """Тест многократного добавления одного продукта"""
        initial_count = Category.product_count

        category_1.add_product(product_1)
        category_1.add_product(product_1)
        category_1.add_product(product_1)

        # Продукт должен добавиться несколько раз (нет проверки на уникальность)
        assert Category.product_count == initial_count + 3
        # Проверяем, что продукт есть в списке (минимум 1 раз)
        assert product_1 in category_1.get_products_list()


class TestCategoryGetTotalQuantity:
    """Тесты для метода get_total_quantity"""

    def test_get_total_quantity_single_product(self, category_2):
        """Тест подсчета количества для категории с одним продуктом"""
        assert category_2.get_total_quantity() == 7  # product_4 quantity = 7

    def test_get_total_quantity_multiple_products(self, category_1):
        """Тест подсчета количества для категории с несколькими продуктами"""
        # product_1: 5, product_2: 8, product_3: 14
        assert category_1.get_total_quantity() == 27  # 5 + 8 + 14

    def test_get_total_quantity_empty_category(self):
        """Тест подсчета количества для пустой категории"""
        empty_category = Category("Empty", "No products", [])
        assert empty_category.get_total_quantity() == 0

    def test_get_total_quantity_after_adding_product(self, category_1, product_4):
        """Тест подсчета количества после добавления продукта"""
        initial_total = category_1.get_total_quantity()  # 27
        category_1.add_product(product_4)  # product_4 quantity = 7
        assert category_1.get_total_quantity() == initial_total + 7


class TestCategoryProductsProperty:
    """Тесты для property products"""

    def test_products_property_format_single(self, category_2):
        """Тест формата вывода для категории с одним продуктом"""
        products_str = category_2.products
        expected = '55" QLED 4K, 123000.0 руб. Остаток: 7 шт.'
        assert products_str == expected

    def test_products_property_format_multiple(self, category_1):
        """Тест формата вывода для категории с несколькими продуктами"""
        products_str = category_1.products
        expected = (
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
            "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
            "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
        )
        assert products_str == expected

    def test_products_property_empty(self):
        """Тест формата вывода для пустой категории"""
        empty_category = Category("Empty", "No products", [])
        expected = "В категории 'Empty' нет продуктов"
        assert empty_category.products == expected

    def test_products_property_after_adding(self, category_1, product_4):
        """Тест обновления property после добавления продукта"""
        initial_products = category_1.products
        category_1.add_product(product_4)
        updated_products = category_1.products

        assert initial_products != updated_products
        assert '55" QLED 4K' in updated_products
        assert len(updated_products.split('\n')) == 4  # Было 3, стало 4


class TestCategoryIntegration:
    """Интеграционные тесты для Category"""

    def test_category_creation_with_products(self, category_1):
        """Тест создания категории с продуктами"""
        products_list = category_1.get_products_list()
        assert len(products_list) == 3
        assert all(isinstance(p, Product) for p in products_list)

    def test_category_counters(self):
        """Тест счетчиков категорий"""
        # Создаем несколько категорий
        cat1 = Category("Cat1", "Desc1", [])
        cat2 = Category("Cat2", "Desc2", [])

        assert Category.category_count >= 2  # Учитывая уже созданные в других тестах
        assert cat1.category_count == Category.category_count
        assert cat2.category_count == Category.category_count

    def test_product_count_increment(self, category_1, product_4):
        """Тест увеличения счетчика продуктов"""
        initial_count = Category.product_count
        category_1.add_product(product_4)
        assert Category.product_count == initial_count + 1