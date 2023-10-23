import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item

        """
        self._name = name  # Название товара
        self.price = price  # Цена за единицу товара
        self.quantity = quantity  # Количество товара в магазине
        Item.all.append(self)  # Хранение экземпляров класса

    def __repr__(self):
        return f"Item('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        """
        Проверка на количество символов больше 10
        """
        if len(value) <= 10:
            self._name = value
        else:
            self._name = value[:10]


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file):
        items = []
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                items.append(item)
            cls.all = items


    @staticmethod
    def string_to_number(number: str):
        return int(float(number))


