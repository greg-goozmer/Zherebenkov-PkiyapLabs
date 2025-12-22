import unittest
from rk1_refactored import Detail, Supplier, Supply, InventoryManager


class TestInventoryManager(unittest.TestCase):
    def setUp(self):
        self.suppliers = [
            Supplier(1, 'Тестовый поставщик 1'),
            Supplier(2, 'Тестовый поставщик 2'),
            Supplier(3, 'Тестовый поставщик без деталей'),
        ]

        self.details = [
            Detail(1, 'Анкер', 100.0, 1),
            Detail(2, 'Арматура', 200.0, 1),
            Detail(3, 'Болт', 50.0, 2),
            Detail(4, 'Амортизатор', 150.0, 2),
        ]

        self.supplies = [
            Supply(1, 1),
            Supply(1, 2),
            Supply(2, 3),
            Supply(2, 4),
        ]

        self.manager = InventoryManager(self.suppliers, self.details, self.supplies)

    def test_get_details_starting_with_a(self):
        """Тест 1: Проверка фильтрации деталей, начинающихся на 'А'"""
        one_to_many = self.manager.create_one_to_many()
        result = self.manager.get_details_starting_with_a(one_to_many)

        for detail in result:
            self.assertTrue(detail[0].startswith('А'))

        self.assertEqual(len(result), 3)

        detail_names = [detail[0] for detail in result]
        self.assertNotIn('Болт', detail_names)

    def test_get_suppliers_with_min_price(self):
        """Тест 2: Проверка поиска минимальной цены у поставщиков"""
        one_to_many = self.manager.create_one_to_many()
        result = self.manager.get_suppliers_with_min_price(one_to_many)

        self.assertEqual(len(result), 2)

        expected_result = [
            ('Тестовый поставщик 2', 50.0),
            ('Тестовый поставщик 1', 100.0),
        ]

        self.assertEqual(result, expected_result)

        prices = [price for _, price in result]
        self.assertEqual(prices, sorted(prices))

    def test_get_sorted_supplies(self):
        """Тест 3: Проверка сортировки поставок"""
        many_to_many = self.manager.create_many_to_many()
        result = self.manager.get_sorted_supplies(many_to_many)

        detail_names = [item[0] for item in result]
        self.assertEqual(detail_names, sorted(detail_names))

        for item in result:
            self.assertEqual(len(item), 3)
            self.assertIsInstance(item[0], str)
            self.assertIsInstance(item[1], float)
            self.assertIsInstance(item[2], str)

        self.assertEqual(len(result), 4)

    def test_empty_data(self):
        empty_manager = InventoryManager([], [], [])
        one_to_many = empty_manager.create_one_to_many()
        many_to_many = empty_manager.create_many_to_many()

        result1 = empty_manager.get_details_starting_with_a(one_to_many)
        result2 = empty_manager.get_suppliers_with_min_price(one_to_many)
        result3 = empty_manager.get_sorted_supplies(many_to_many)

        self.assertEqual(len(result1), 0)
        self.assertEqual(len(result2), 0)
        self.assertEqual(len(result3), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)