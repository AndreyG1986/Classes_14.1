def test_init(product_tomato):
    assert product_tomato.name == "tomato"
    assert product_tomato.description == "red and cool"
    assert product_tomato.price == 100.28
    assert product_tomato.quantity == 4