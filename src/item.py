class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


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
        self.price = self.price*Item.pay_rate/100

