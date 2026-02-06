from src.main import Category



def test_init_category(category_1, category_2):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    # Здесь уже не будет ошибки, так как мы добавили продукты через add_product
    # assert category_1.products == [product_1, product_2, product_3]
    # # Проверяем количество товаров в ЭТОЙ категории
    # # Для этого добавим свойство в класс или просто проверяем длину списка
    # assert len(category_1.products) == 3
    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    # assert category_2.products == [product_4]
    # assert len(category_2.products) == 1
    assert Category.category_count == 2
