"""Inventory stock tracking and reservation."""

RESERVATION_TTL_SECONDS = 900


class OversellError(Exception):
    pass


class Stock:
    def __init__(self, sku, available):
        self.sku = sku
        self.available = available

    def reserve(self, quantity):
        if quantity > self.available:
            raise OversellError(
                "cannot reserve %d of %s, only %d available"
                % (quantity, self.sku, self.available)
            )
        self.available -= quantity
        return {"sku": self.sku, "reserved": quantity, "remaining": self.available}

    def restock(self, quantity):
        if quantity < 0:
            raise ValueError("restock quantity must be non-negative")
        self.available += quantity
        return self.available


def describe(stock):
    label = "%s: %d available" % (stock.sku, stock.available)
    return label
