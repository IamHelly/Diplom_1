from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from praktikum.burger import Burger
from unittest.mock import Mock
import pytest
from typing import List


class TestBurger:
    def test_set_buns_set_new_bun(self):
        burger = Burger()
        bun_mock = Mock()
        bun_mock.configure_mock(name='Биг-маг с двойной котлетой', price=280.50)
        burger.set_buns(bun_mock)
        assert burger.bun == bun_mock

    def test_add_ingredient_add_three_ingredients(self):
        burger = Burger()
        ingredient_1_mock = Mock()
        ingredient_2_mock = Mock()
        ingredient_3_mock = Mock()
        ingredient_1_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, nama='Куриная котлета', price=99.85)
        ingredient_2_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, name='Кружочек помидора', price=15)
        ingredient_3_mock.configure_mock(type=INGREDIENT_TYPE_SAUCE, name='Сырный соус', price=20.45)
        burger.add_ingredient(ingredient_1_mock)
        burger.add_ingredient(ingredient_2_mock)
        burger.add_ingredient(ingredient_3_mock)
        assert len(burger.ingredients) == 3

    def test_remove_ingredient_remove_one_ingredient(self):
        burger = Burger()
        ingredient_1_mock = Mock()
        ingredient_1_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, name='Лук репчатый', price=3.45)
        burger.add_ingredient(ingredient_1_mock)
        burger.remove_ingredient(-1)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_move_ingredient_to_the_second_index(self):
        burger = Burger()
        ingredient_1_mock = Mock()
        ingredient_2_mock = Mock()
        ingredient_3_mock = Mock()
        ingredient_1_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, nama='Куриная котлета', price=99.85)
        ingredient_2_mock.configure_mock(type=INGREDIENT_TYPE_FILLING, name='Кружочек помидора', price=15)
        ingredient_3_mock.configure_mock(type=INGREDIENT_TYPE_SAUCE, name='Сырный соус', price=20.45)
        burger.add_ingredient(ingredient_1_mock)
        burger.add_ingredient(ingredient_2_mock)
        burger.add_ingredient(ingredient_3_mock)
        burger.move_ingredient(2, 1)
        assert burger.ingredients == [ingredient_1_mock, ingredient_3_mock, ingredient_2_mock]

    @pytest.mark.parametrize('price_1, price_2, price_3, price_4, sum', [
        [100.50, 23.99, 180.50, 68.50, 473.99],
        [33.00, 75.90, 10.50, 210.45, 362.85],
    ])
    def test_get_price_get_finalize_the_price(self, price_1, price_2, price_3, price_4, sum):
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_price.return_value = price_1
        ingredient_1_mock = Mock(spec=Ingredient)
        ingredient_2_mock = Mock(spec=Ingredient)
        ingredient_3_mock = Mock(spec=Ingredient)
        ingredient_1_mock.get_price.return_value = price_2
        ingredient_2_mock.get_price.return_value = price_3
        ingredient_3_mock.get_price.return_value = price_4
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_1_mock)
        burger.add_ingredient(ingredient_2_mock)
        burger.add_ingredient(ingredient_3_mock)
        assert burger.get_price() == sum

    def test_get_receipt_get_receipt_for_the_bun(self):
        receipt_new: List[str] = []
        burger = Burger()
        bun_mock = Mock(spec=Bun)
        bun_mock.get_name.return_value = 'Чиабатта по-грузински'
        receipt_new.append(f'(==== {bun_mock.get_name.return_value} ====)')
        bun_mock.get_price.return_value = 145.99
        ingredient_1_mock = Mock()
        ingredient_2_mock = Mock()
        ingredient_1_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient_2_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient_1_mock.get_name.return_value = 'Консервированная фасоль'
        ingredient_2_mock.get_name.return_value = 'Сацебели'
        receipt_new.append(f'= {ingredient_1_mock.get_type.return_value.lower()} {ingredient_1_mock.get_name.return_value} =')
        receipt_new.append(f'= {ingredient_2_mock.get_type.return_value.lower()} {ingredient_2_mock.get_name.return_value} =')
        ingredient_1_mock.get_price.return_value = 2.50
        ingredient_2_mock.get_price.return_value = 8.99
        receipt_new.append(f'(==== {bun_mock.get_name.return_value} ====)\n')
        receipt_new.append(f'Price: 303.47')
        burger.set_buns(bun_mock)
        burger.add_ingredient(ingredient_1_mock)
        burger.add_ingredient(ingredient_2_mock)
        assert burger.get_receipt() == '\n'.join(receipt_new)
