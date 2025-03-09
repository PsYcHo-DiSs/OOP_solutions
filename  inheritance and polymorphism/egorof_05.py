from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class Product:
    name: str
    price: float = field(repr=False)

    def __hash__(self):
        return hash((self.name, self.price))

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name and self.price == other.price


@dataclass
class Promo:
    title: str
    disc_value: int
    products: list = field(default_factory=list)

    def __post_init__(self):
        # Убедимся, что скидка в пределах допустимого диапазона
        if not (1 <= self.disc_value <= 100):
            self.disc_value = 0


class Cart:
    def __init__(self):
        self.cart = defaultdict(int)  # Словарь для хранения товара и его количества
        self.discount = 0
        self.applied_promo = None  # Чтобы отслеживать примененный промокод

    def add_product(self, prod, quantity=1):
        if not isinstance(prod, Product):
            raise TypeError("Можно добавлять только объекты Product")
        self.cart[prod] += quantity

    def get_total(self):
        total_price = sum(p.price * quantity for p, quantity in self.cart.items())

        # Применение промокода, если он существует
        if self.applied_promo:
            promo = self.applied_promo
            # Применяется промокод только к определенным товарам или ко всей корзине
            if promo.products:  # Применяется только к определенным товарам
                total_discount = 0
                for product in promo.products:
                    if product in self.cart:
                        total_discount += product.price * self.cart[product] * promo.disc_value / 100
                total_price -= total_discount
            else:  # Применяется ко всей корзине
                total_price -= total_price * promo.disc_value / 100
            self.reset_promo()  # Сброс промокода

        else:
            # Применение общей скидки
            total_price *= (1 - self.discount / 100)

        return total_price

    def apply_discount(self, disc_value):
        if not isinstance(disc_value, int) or not (1 <= disc_value <= 100):
            raise ValueError('Неправильное значение скидки')
        # Сбрасываем промокод при применении прямой скидки
        self.reset_promo()
        self.discount = disc_value

    def apply_promo(self, promo_title):
        # Поиск подходящего промокода в ACTIVE_PROMO
        promo_to_check = next((p for p in ACTIVE_PROMO if promo_title == p.title), None)
        if promo_to_check:
            self.applied_promo = promo_to_check
            print(f'Промокод {promo_title} успешно применился')
        else:
            print(f"Промокода {promo_title} не существует")

    def reset_promo(self):
        self.applied_promo = None
