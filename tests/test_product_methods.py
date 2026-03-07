import pytest
from src.main import Product


class TestProductPriceSetter:
    """Тесты для price setter"""

    def test_price_setter_positive(self, product_1):
        """Тест установки положительной цены"""
        product_1.price = 200000.0
        assert product_1.price == 200000.0

    def test_price_setter_zero(self, product_1, capsys):
        """Тест установки нулевой цены (должен вывести предупреждение)"""
        product_1.price = 0
        captured = capsys.readouterr()
        assert product_1.price == 180000.0  # Цена не изменилась
        assert "Цена не должна быть нулевая или отрицательная" in captured.out

    def test_price_setter_negative(self, product_1, capsys):
        """Тест установки отрицательной цены (должен вывести предупреждение)"""
        product_1.price = -100
        captured = capsys.readouterr()
        assert product_1.price == 180000.0  # Цена не изменилась
        assert "Цена не должна быть нулевая или отрицательная" in captured.out


class TestProductNewProduct:
    """Тесты для classmethod new_product"""

    def test_new_product_creation(self):
        """Тест создания продукта через класс-метод"""
        product_data = {"name": "Test Product", "description": "Test Description", "price": 1000.0, "quantity": 10}
        product = Product.new_product(product_data)

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 1000.0
        assert product.quantity == 10

    def test_new_product_with_invalid_data_type(self):
        """Тест создания продукта с некорректным типом данных"""
        with pytest.raises(TypeError, match="Данные должны быть представлены в виде словаря"):
            Product.new_product(["not", "a", "dict"])

    def test_new_product_missing_fields(self):
        """Тест создания продукта с отсутствующими полями"""
        product_data = {
            "name": "Test Product"
            # Остальные поля отсутствуют
        }
        # Изменяем ожидание с "price" на "description", так как description отсутствует первым
        with pytest.raises(ValueError, match="Отсутствует обязательное поле: description"):
            Product.new_product(product_data)

    def test_new_product_with_extra_fields(self, product_1):
        """Тест создания продукта с лишними полями"""
        product_data = {
            "name": "Extra Product",
            "description": "With extra fields",
            "price": 500.0,
            "quantity": 3,
            "extra_field": "should be ignored",
            "another_field": 123,
        }
        product = Product.new_product(product_data)

        assert product.name == "Extra Product"
        assert product.description == "With extra fields"
        assert product.price == 500.0
        assert product.quantity == 3
        # Проверяем, что лишних атрибутов нет
        assert not hasattr(product, "extra_field")
        assert not hasattr(product, "another_field")
