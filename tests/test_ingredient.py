from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    def test_get_price_get_price_the_ingredient(self):
        name_ingredient = 'Кетчуп'
        price_ingredient = 18.50
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name_ingredient, price_ingredient)
        assert ingredient.get_price() == 18.50

    def test_get_name_get_name_the_ingredient(self):
        name_ingredient = 'Рыбная котлета'
        price_ingredient = 99.99
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, name_ingredient, price_ingredient)
        assert ingredient.get_name() == 'Рыбная котлета'

    def test_get_type_get_type_of_ingredient_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Чесночный соус', 5.00)
        assert ingredient.get_type() == 'SAUCE'

    def test_get_type_get_type_of_ingredient_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Маринованный огурец', 2.50)
        assert ingredient.get_type() == 'FILLING'
