"""Shopping cart model."""

MAX_CART_ITEMS = 50


class Item:
    def __init__(self, sku, price_cents, qty):
        self.sku = sku
        self.price_cents = price_cents
        self.qty = qty


class Cart:
    def __init__(self, card_token, items):
        self.card_token = card_token
        self.items = items

    def total_cents(self):
        total_cents = sum(item.price_cents * item.qty for item in self.items)
        if total_cents <= 0:
            raise ValueError("cart total must be positive")
        return total_cents

    def add_item(self, item):
        if len(self.items) > MAX_CART_ITEMS:
            raise ValueError("cart is full")
        self.items.append(item)
