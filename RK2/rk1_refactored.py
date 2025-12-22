from operator import itemgetter


class Detail:
    def __init__(self, id, name, price, supplier_id):
        self.id = id
        self.name = name
        self.price = price
        self.supplier_id = supplier_id


class Supplier:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Supply:
    def __init__(self, supplier_id, detail_id):
        self.supplier_id = supplier_id
        self.detail_id = detail_id


class InventoryManager:
    def __init__(self, suppliers, details, supplies):
        self.suppliers = suppliers
        self.details = details
        self.supplies = supplies

    def create_one_to_many(self):
        """Создание связи один-ко-многим"""
        return [(d.name, d.price, s.name)
                for s in self.suppliers
                for d in self.details
                if d.supplier_id == s.id]

    def create_many_to_many(self):
        many_to_many_temp = [(s.name, sup.supplier_id, sup.detail_id)
                             for s in self.suppliers
                             for sup in self.supplies
                             if s.id == sup.supplier_id]

        return [(d.name, d.price, supplier_name)
                for supplier_name, supplier_id, detail_id in many_to_many_temp
                for d in self.details if d.id == detail_id]

    def get_details_starting_with_a(self, one_to_many):
        """Задание B1: Детали, начинающиеся на 'А'"""
        return list(filter(lambda i: i[0].startswith('А'), one_to_many))

    def get_suppliers_with_min_price(self, one_to_many):
        """Задание B2: Поставщики с минимальной ценой детали"""
        res2_unsorted = []
        for s in self.suppliers:
            s_details = list(filter(lambda i: i[2] == s.name, one_to_many))
            if len(s_details) > 0:
                s_prices = [price for _, price, _ in s_details]
                min_price = min(s_prices)
                res2_unsorted.append((s.name, min_price))

        return sorted(res2_unsorted, key=itemgetter(1))

    def get_sorted_supplies(self, many_to_many):
        """Задание B3: Отсортированные поставки"""
        return sorted(many_to_many, key=itemgetter(0))


def load_test_data():
    suppliers = [
        Supplier(1, 'Авиатехно'),
        Supplier(2, 'Автодеталь'),
        Supplier(3, 'Металлопрокат'),
        Supplier(4, 'Станкоимпорт'),
        Supplier(5, 'Техносила'),
    ]

    details = [
        Detail(1, 'Анкерный болт', 28.90, 1),
        Detail(2, 'Гайка М10', 8.30, 2),
        Detail(3, 'Шайба 10мм', 5.20, 2),
        Detail(4, 'Винт М6', 12.10, 3),
        Detail(5, 'Подшипник 6305', 245.00, 4),
        Detail(6, 'Амортизатор', 320.75, 4),
        Detail(7, 'Арматура А1', 45.80, 1),
    ]

    supplies = [
        Supply(1, 1),
        Supply(1, 7),
        Supply(2, 2),
        Supply(2, 3),
        Supply(3, 4),
        Supply(4, 5),
        Supply(4, 6),
        Supply(5, 1),
        Supply(5, 4),
    ]

    return suppliers, details, supplies


def main():
    suppliers, details, supplies = load_test_data()
    manager = InventoryManager(suppliers, details, supplies)

    one_to_many = manager.create_one_to_many()
    many_to_many = manager.create_many_to_many()

    print("Задание B1:")
    res1 = manager.get_details_starting_with_a(one_to_many)
    print(res1)

    print('\nЗадание B2:')
    res2 = manager.get_suppliers_with_min_price(one_to_many)
    print(res2)

    print('\nЗадание B3:')
    res3 = manager.get_sorted_supplies(many_to_many)
    print(res3)


if __name__ == '__main__':
    main()