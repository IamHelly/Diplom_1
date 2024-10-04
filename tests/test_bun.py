from praktikum.bun import Bun


class TestBun:

    def test_get_name_get_name_the_bun(self):
        bun_name = 'Датский хот-дог'
        bun = Bun(bun_name, 299.99)
        assert bun.get_name() == bun_name

    def test_get_price_get_price_the_bun(self):
        bun = Bun('Биг Тейсти', 350)
        assert bun.get_price() == 350
