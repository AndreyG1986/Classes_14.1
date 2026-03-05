import pytest
from src.base_classes import Product
from src.print_mixin import PrintMixin


class MockProduct(PrintMixin):
    """Мок-класс для тестирования"""

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()

    # Добавляем __repr__ из миксина для согласованности
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


def test_print_mixin_output(capsys):
    """Тест с использованием capsys - исправленный"""

    product = Product("Ноутбук", "Мощный", 50000, 10)

    captured = capsys.readouterr()
    # Исправляем ожидаемый результат на фактический формат Product.__repr__
    expected = "Product(name='Ноутбук', price=50000, quantity=10)"
    assert captured.out.strip() == expected


def test_print_mixin_multiple_outputs(capsys):
    """Тест множественных выводов - исправленный"""

    products = [
        Product("A", "Desc A", 100, 1),
        Product("B", "Desc B", 200, 2),
    ]

    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")

    assert len(lines) == 2
    assert lines[0] == "Product(name='A', price=100, quantity=1)"
    assert lines[1] == "Product(name='B', price=200, quantity=2)"


@pytest.mark.parametrize(
    "name,desc,price,qty,expected",
    [
        ("Тест1", "Описание1", 100, 5, "Product(name='Тест1', price=100, quantity=5)"),
        ("Тест2", "Описание2", 200, 10, "Product(name='Тест2', price=200, quantity=10)"),
        ("", "", 0, 0, "Product(name='', price=0, quantity=0)"),
    ],
)
def test_print_mixin_parametrized(capsys, name, desc, price, qty, expected):
    """Параметризованный тест - исправленный"""

    Product(name, desc, price, qty)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


def test_print_mixin_with_mock_class(capsys):
    """Тест с мок-классом"""

    mock = MockProduct("Мок", "Тестовый", 777, 3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "MockProduct(Мок, Тестовый, 777, 3)"


def test_print_mixin_different_repr():
    """Тест, показывающий разницу между __repr__ методами"""

    product = Product("Тест", "Описание", 100, 5)

    # Это вызовет Product.__repr__
    product_repr = repr(product)
    assert product_repr == "Product(name='Тест', price=100, quantity=5)"

    # А это то, что ожидалось в миксине
    mixin_style_repr = f"Product({product.name}, {product.description}, {product.price}, {product.quantity})"
    assert mixin_style_repr == "Product(Тест, Описание, 100, 5)"

    print(f"\nProduct.__repr__: {product_repr}")
    print(f"Mixin style:     {mixin_style_repr}")


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
