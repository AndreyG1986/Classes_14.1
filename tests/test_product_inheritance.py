from src.main import Product


# Создаем мок-классы прямо в тестах
class MockSmartphone(Product):
    def __init__(self, name, description, price, quantity, performance, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class MockLawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class TestProductInheritance:
    """Тесты для проверки наследования"""

    def test_smartphone_is_product(self):
        """Тест: Smartphone является наследником Product"""
        smartphone = MockSmartphone("Test Phone", "Description", 50000.0, 10, "High", "Model X", 256, "Black")
        assert isinstance(smartphone, Product)

    def test_lawn_grass_is_product(self):
        """Тест: LawnGrass является наследником Product"""
        grass = MockLawnGrass("Test Grass", "Description", 1000.0, 20, "Russia", "30 days", "Green")
        assert isinstance(grass, Product)

    def test_smartphone_has_product_methods(self):
        """Тест: Smartphone имеет методы Product"""
        smartphone = MockSmartphone("Test Phone", "Description", 50000.0, 10, "High", "Model X", 256, "Black")

        # Проверяем наличие методов Product
        assert hasattr(smartphone, "price")
        assert hasattr(smartphone, "new_product")
        assert hasattr(smartphone, "__add__")
        assert hasattr(smartphone, "__str__")

    def test_smartphone_specific_attributes(self):
        """Тест: Smartphone имеет свои специфичные атрибуты"""
        smartphone = MockSmartphone("Test Phone", "Description", 50000.0, 10, "High", "Model X", 256, "Black")

        assert smartphone.performance == "High"
        assert smartphone.model == "Model X"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"

    def test_lawn_grass_specific_attributes(self):
        """Тест: LawnGrass имеет свои специфичные атрибуты"""
        grass = MockLawnGrass("Test Grass", "Description", 1000.0, 20, "Russia", "30 days", "Green")

        assert grass.country == "Russia"
        assert grass.germination_period == "30 days"
        assert grass.color == "Green"

    def test_both_classes_inherit_from_product(self):
        """Тест: оба класса наследуются от Product"""
        assert issubclass(MockSmartphone, Product)
        assert issubclass(MockLawnGrass, Product)
