import typing as tp

from .types import Currency


class Item:
    def __init__(self, name: str, price: float | int, currency: Currency, description: str):
        self.name = name
        self.price = price
        self.currency = currency.value
        self.description = description

    @classmethod
    def generate_samples(cls) -> list[tp.Self]:
        return [
            cls("Клавиатура", 1099.99, Currency.RUR, "Крутая клавиатура"),
            cls("Телевизор", 1_000, Currency.USD, "Крутой телевизор"),
            cls("Холодильник", 25_000, Currency.RUR, "Новый холодильник"),
        ]