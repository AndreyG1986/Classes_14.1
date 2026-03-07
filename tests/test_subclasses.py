import pytest
from src.subclasses import Smartphone, LawnGrass
from src.base_classes import Product


class TestSmartphone:
    """Тесты для класса Smartphone"""

    def test_smartphone_creation(self):
        """Тест создания объекта Smartphone"""
        phone = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
        )

        # Проверяем атрибуты от Product
        assert phone.name == "Samsung Galaxy S23 Ultra"
        assert phone.description == "256GB, Серый цвет, 200MP камера"
        assert phone.price == 180000.0
        assert phone.quantity == 5

        # Проверяем новые атрибуты
        assert phone.efficiency == 95.5
        assert phone.model == "S23 Ultra"
        assert phone.memory == 256
        assert phone.color == "Серый"

    def test_smartphone_is_instance_of_product(self):
        """Тест проверки наследования"""
        phone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

        # Проверяем, что Smartphone является наследником Product
        assert isinstance(phone, Product)
        assert isinstance(phone, Smartphone)

    def test_smartphone_zero_quantity_raises_error(self):
        """Тест создания смартфона с нулевым количеством"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            Smartphone(
                "Test Phone", "Test Description", 1000.0, 0, 95.5, "Test Model", 128, "Black"  # Нулевое количество
            )

    def test_smartphone_price_setter(self):
        """Тест установки цены для смартфона"""
        phone = Smartphone("Test Phone", "Test Description", 1000.0, 5, 95.5, "Test Model", 128, "Black")

        # Устанавливаем новую цену
        phone.price = 1500.0
        assert phone.price == 1500.0

        # Пытаемся установить отрицательную цену
        phone.price = -100
        assert phone.price == 1500.0  # Цена не изменилась

    def test_smartphone_str_repr(self, capsys):
        """Тест строкового представления смартфона"""
        phone = Smartphone("Test Phone", "Test Description", 1000.0, 5, 95.5, "Test Model", 128, "Black")

        # Проверяем __str__ метод (наследуется от Product)
        assert str(phone) == "Test Phone, 1000.0 руб. Остаток: 5 шт."

        # Проверяем __repr__ метод (наследуется от Product)
        assert repr(phone) == "Product(name='Test Phone', price=1000.0, quantity=5)"


class TestLawnGrass:
    """Тесты для класса LawnGrass"""

    def test_lawn_grass_creation(self):
        """Тест создания объекта LawnGrass"""
        grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")

        # Проверяем атрибуты от Product
        assert grass.name == "Газонная трава"
        assert grass.description == "Элитная трава для газона"
        assert grass.price == 500.0
        assert grass.quantity == 20

        # Проверяем новые атрибуты
        assert grass.country == "Россия"
        assert grass.germination_period == "7 дней"
        assert grass.color == "Зеленый"

    def test_lawn_grass_is_instance_of_product(self):
        """Тест проверки наследования"""
        grass = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

        # Проверяем, что LawnGrass является наследником Product
        assert isinstance(grass, Product)
        assert isinstance(grass, LawnGrass)

    def test_lawn_grass_zero_quantity_raises_error(self):
        """Тест создания травы с нулевым количеством"""
        with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
            LawnGrass("Test Grass", "Test Description", 100.0, 0, "Россия", "5 дней", "Зеленый")  # Нулевое количество

    def test_lawn_grass_price_setter(self):
        """Тест установки цены для травы"""
        grass = LawnGrass("Test Grass", "Test Description", 100.0, 10, "Россия", "5 дней", "Зеленый")

        # Устанавливаем новую цену
        grass.price = 150.0
        assert grass.price == 150.0

        # Пытаемся установить отрицательную цену
        grass.price = -50
        assert grass.price == 150.0  # Цена не изменилась

    def test_lawn_grass_str_repr(self, capsys):
        """Тест строкового представления травы"""
        grass = LawnGrass("Test Grass", "Test Description", 100.0, 10, "Россия", "5 дней", "Зеленый")

        # Проверяем __str__ метод (наследуется от Product)
        assert str(grass) == "Test Grass, 100.0 руб. Остаток: 10 шт."

        # Проверяем __repr__ метод (наследуется от Product)
        assert repr(grass) == "Product(name='Test Grass', price=100.0, quantity=10)"


class TestInheritance:
    """Тесты для проверки наследования"""

    def test_smartphone_has_product_methods(self):
        """Тест наличия методов Product у Smartphone"""
        phone = Smartphone("Test Phone", "Test Description", 1000.0, 5, 95.5, "Test Model", 128, "Black")

        # Проверяем наличие методов от Product
        assert hasattr(phone, "price")
        assert hasattr(phone, "new_product")
        assert hasattr(phone, "__add__")

    def test_lawn_grass_has_product_methods(self):
        """Тест наличия методов Product у LawnGrass"""
        grass = LawnGrass("Test Grass", "Test Description", 100.0, 10, "Россия", "5 дней", "Зеленый")

        # Проверяем наличие методов от Product
        assert hasattr(grass, "price")
        assert hasattr(grass, "new_product")
        assert hasattr(grass, "__add__")

    def test_multiple_smartphones_creation(self):
        """Тест создания нескольких смартфонов"""
        phones = [
            Smartphone("Phone1", "Desc1", 100.0, 1, 90.0, "Model1", 64, "Red"),
            Smartphone("Phone2", "Desc2", 200.0, 2, 95.0, "Model2", 128, "Blue"),
            Smartphone("Phone3", "Desc3", 300.0, 3, 98.0, "Model3", 256, "Black"),
        ]

        assert len(phones) == 3
        assert phones[0].name == "Phone1"
        assert phones[1].memory == 128
        assert phones[2].color == "Black"
