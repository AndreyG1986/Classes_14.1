import pytest

from src.main import Product

@pytest.fixture()
def product_tomato():
    return Product("tomato","red and cool",100.28,4)