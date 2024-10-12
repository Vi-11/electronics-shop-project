from bokeh.core.property.bases import Property
from sipbuild.generator.parser.annotations import integer
from tifffile import astype


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name[0:11]
    @classmethod
    def instantiate_from_csv(cls, path):
        import csv
        with open(file=r'E:\electronics-shop-project\src\items.csv',encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                a=cls(row['name'],row['price'],row['quantity'])
    @staticmethod
    def string_to_number(str):
        return int(float(str))

    def calculate_total_price(self) -> float:
        """
        Возвращает полную стоимость всех товаров
        """
        total = self.quantity * self.price
        return total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*Item.pay_rate

