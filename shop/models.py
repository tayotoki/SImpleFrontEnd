import dataclasses
import typing as tp
from datetime import datetime

from .types import Currency


@dataclasses.dataclass
class Item:
    name: str
    price: float | int
    currency: Currency
    description: str

    @classmethod
    def generate_samples(cls) -> list[tp.Self]:
        return [
            cls("Клавиатура", 1099.99, Currency.RUR, "Крутая клавиатура"),
            cls("Телевизор", 1_000, Currency.USD, "Крутой телевизор"),
            cls("Холодильник", 25_000, Currency.RUR, "Новый холодильник"),
        ]


@dataclasses.dataclass
class Category:
    name: str

    @classmethod
    def generate_samples(cls) -> list[tp.Self]:
        return [
            cls("Техника"),
            cls("Бытовая химия"),
            cls("Одежда"),
        ]


@dataclasses.dataclass
class Order:
    item: Item
    user: str
    date: datetime

    @classmethod
    def generate_samples(cls) -> list[tp.Self]:
        return [
            cls(*data) for data in zip(
                Item.generate_samples(),
                ["test_user_1", "test_user_2", "test_user_3"],
                [datetime.now(),
                 datetime.now().replace(day=datetime.now().day + 1),
                 datetime.now().replace(day=datetime.now().day + 2)]
            )
        ]