from src.main import Category, Product


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
        assert category_1.products == [product_1, product_2, product_3]
        assert len(category_1.products) == 3

        assert category_2.name == "Телевизоры"
        assert (
                category_2.description
                == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
        )
        assert category_2.products == [product_4]
        assert len(category_2.products) == 1

    def test_category_counters(self):
        """Тестирование счетчиков категорий и товаров"""
        # Создаем тестовые товары
        product1 = Product("Товар1", "Описание1", 1000.0, 5)
        product2 = Product("Товар2", "Описание2", 2000.0, 3)
        product3 = Product("Товар3", "Описание3", 3000.0, 2)

        # Создаем категории
        category1 = Category("Категория1", "Описание1", [product1, product2])
        category2 = Category("Категория2", "Описание2", [product3])

        # Проверяем счетчики
        assert Category.category_count == 2
        assert Category.product_count == 3  # 2 + 1 = 3

    def test_empty_category(self):
        """Тестирование создания категории без товаров"""
        empty_category = Category("Пустая категория", "Описание пустой категории", [])

        assert empty_category.name == "Пустая категория"
        assert empty_category.description == "Описание пустой категории"
        assert empty_category.products == []
        assert len(empty_category.products) == 0

        # Проверяем, что счетчики увеличились
        assert Category.category_count == 1
        assert Category.product_count == 0  # Без изменений, так как товаров нет

    def test_category_with_none_products(self):
        """Тестирование категории с None вместо списка товаров"""
        # Сохраняем текущие счетчики
        initial_category_count = Category.category_count
        initial_product_count = Category.product_count

        category = Category("Категория", "Описание", None)

        assert category.products is None
        # Проверяем, что счетчики изменились
        assert Category.category_count == initial_category_count + 1
        assert Category.product_count == initial_product_count  # Не увеличился

    def test_category_products_modification(self):
        """Тестирование модификации списка товаров"""
        product = Product("Товар", "Описание", 1000.0, 5)
        category = Category("Категория", "Описание", [product])

        initial_count = len(category.products)
        initial_product_count = Category.product_count

        # Добавляем новый товар
        new_product = Product("Новый телефон", "Описание", 50000.0, 10)
        category.products.append(new_product)

        assert len(category.products) == initial_count + 1
        assert new_product in category.products
        # product_count не должен меняться при модификации списка
        assert Category.product_count == initial_product_count

    def test_category_str_repr(self):
        """Тестирование строкового представления категории"""
        product = Product("Товар", "Описание", 1000.0, 5)
        category = Category("Тестовая категория", "Описание категории", [product])

        str_representation = str(category)
        repr_representation = repr(category)

        assert category.name in str_representation
        assert "количество продуктов" in str_representation
        assert category.name in repr_representation
        assert "Category" in repr_representation

    def test_category_product_access(self):
        """Тестирование доступа к товарам в категории"""
        product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        category = Category("Смартфоны", "Описание", [product1, product2, product3])

        # Проверяем доступ по индексу
        assert category.products[0].name == "Samsung Galaxy S23 Ultra"
        assert category.products[1].price == 210000.0
        assert category.products[2].quantity == 14

    def test_category_with_duplicate_products(self):
        """Тестирование категории с дублирующимися товарами"""
        product = Product("Товар", "Описание", 1000.0, 5)
        category = Category("Категория", "Описание", [product, product, product])

        assert len(category.products) == 3
        # Все три элемента - один и тот же объект
        assert category.products[0] is category.products[1]
        assert category.products[1] is category.products[2]
        # В текущей реализации product_count увеличивается на длину списка
        # независимо от уникальности объектов
        assert Category.product_count == 3

    def test_category_attributes_types(self):
        """Тестирование типов атрибутов категории"""
        product = Product("Товар", "Описание", 1000.0, 5)
        category = Category("Категория", "Описание категории", [product])

        assert isinstance(category.name, str)
        assert isinstance(category.description, str)
        assert isinstance(category.products, list)
        assert isinstance(Category.category_count, int)
        assert isinstance(Category.product_count, int)

    def test_multiple_categories_independent(self):
        """Тестирование независимости разных категорий"""
        product1 = Product("Товар1", "Описание1", 1000.0, 5)
        product2 = Product("Товар2", "Описание2", 2000.0, 3)

        category1 = Category("Категория1", "Описание1", [product1])
        category2 = Category("Категория2", "Описание2", [product2])

        # Категории должны быть независимы
        assert category1.name != category2.name
        assert category1.products != category2.products
        assert len(category1.products) == 1
        assert len(category2.products) == 1
        assert Category.category_count == 2
        assert Category.product_count == 2

    def test_category_with_empty_strings(self):
        """Тестирование категории с пустыми строками"""
        category = Category("", "", [])

        assert category.name == ""
        assert category.description == ""
        assert category.products == []
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_product_count_behavior(self):
        """Тестирование поведения счетчика товаров"""
        # Проверяем, что счетчик увеличивается на длину списка
        assert Category.product_count == 0

        # Создаем 3 уникальных товара
        products = [
            Product("Товар1", "Описание1", 1000.0, 5),
            Product("Товар2", "Описание2", 2000.0, 3),
            Product("Товар3", "Описание3", 3000.0, 2)
        ]

        category = Category("Категория", "Описание", products)
        assert Category.product_count == 3  # Увеличилось на 3

        # Создаем еще одну категорию с теми же товарами
        category2 = Category("Категория2", "Описание2", products)
        assert Category.product_count == 6  # Увеличилось еще на 3

        # Создаем категорию с пустым списком
        category3 = Category("Пустая", "Описание", [])
        assert Category.product_count == 6  # Не изменилось


# Отдельные тесты без класса
def test_category_initial_counters():
    """Тестирование начальных значений счетчиков"""
    # Сбрасываем счетчики для этого теста
    Category.category_count = 0
    Category.product_count = 0

    assert Category.category_count == 0
    assert Category.product_count == 0


def test_category_product_addition_updates_counters():
    """Тестирование что добавление товаров обновляет счетчики"""
    # Сбрасываем счетчики
    Category.category_count = 0
    Category.product_count = 0

    # Создаем товары
    products = [
        Product("Товар1", "Описание1", 1000.0, 5),
        Product("Товар2", "Описание2", 2000.0, 3),
        Product("Товар3", "Описание3", 3000.0, 2)
    ]

    # Создаем категорию с 3 товарами
    category = Category("Категория", "Описание", products)

    assert Category.category_count == 1
    assert Category.product_count == 3


def test_product_count_counts_all_instances():
    """Тестирование что product_count считает все экземпляры товаров"""
    Category.category_count = 0
    Category.product_count = 0

    # Один и тот же товарный объект в нескольких категориях
    shared_product = Product("Общий товар", "Описание", 1000.0, 5)

    # Создаем несколько категорий с тем же товаром
    category1 = Category("Категория1", "Описание1", [shared_product])
    assert Category.product_count == 1

    category2 = Category("Категория2", "Описание2", [shared_product])
    assert Category.product_count == 2  # Увеличивается, хотя объект тот же

    category3 = Category("Категория3", "Описание3", [shared_product, shared_product])
    assert Category.product_count == 4  # Увеличивается на 2
