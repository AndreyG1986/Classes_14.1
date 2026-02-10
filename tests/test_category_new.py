from src.main import Category


class TestCategory:
    """Класс для тестирования Category с изолированными счетчиками"""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом"""
        Category.category_count = 0
        Category.product_count = 0

    def test_init_category(self, product_1, product_2, product_3, product_4):
        """Тестирование базовой инициализации категорий"""
        category_1 = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [product_1, product_2, product_3],
        )

        category_2 = Category(
            "Телевизоры",
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            [product_4],
        )

        assert category_1.name == "Смартфоны"
        assert (
            category_1.description
            == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
        )
        # Вместо обращения к products, используем products_info
        product_info = category_1.products_info
        assert "Samsung Galaxy S23 Ultra" in product_info
        assert "Iphone 15" in product_info
        assert "Xiaomi Redmi Note 11" in product_info

        assert category_2.name == "Телевизоры"
        assert (
            category_2.description
            == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        )
        assert '55" QLED 4K' in category_2.products_info

    def test_empty_category(self):
        """Тестирование создания категории без товаров"""
        empty_category = Category("Пустая категория", "Описание пустой категории", [])

        assert empty_category.name == "Пустая категория"
        assert empty_category.description == "Описание пустой категории"
        assert "нет продуктов" in empty_category.products_info
