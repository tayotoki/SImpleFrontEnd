import dataclasses
import decimal
import typing as tp
from datetime import datetime

from .types import Currency, Statuses


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
            cls("Свитер", 2_599, Currency.RUR, "Классный свитер"),
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
    number: int
    item: Item
    price: int | float
    amount: int
    date: datetime
    status: Statuses
    full_price: decimal.Decimal = dataclasses.field(init=False)

    def __post_init__(self):
        self.full_price = decimal.Decimal(self.price * self.amount).quantize(decimal.Decimal("1.00"))

    @classmethod
    def generate_samples(cls) -> list[tp.Self]:
        items = Item.generate_samples()

        return [
            cls(
                number=i + 1,
                item=items[i],
                price=items[i].price,
                amount=i + 1,
                date=datetime.now().replace(day=datetime.now().day + i),
                status=status,
            ) for i, status in enumerate(Statuses)
        ]


@dataclasses.dataclass
class FAQ:
    title: str
    answer: str

    @classmethod
    def get_samples(cls) -> list[tp.Self]:
        return [
            cls("Где купить?", "Большой текст о том как купить товар"),
            cls("Как доставить", "Текст о крутой системе доставки магазина"),
            cls("Какая гарантия?", "Блок текста о великолепной гарантии, возврат средств 100%"),
        ]

    def get_html_safe_id(self):
        return "".join(self.title.split())
