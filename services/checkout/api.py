"""Checkout API: validates and charges carts."""

from services.payments import client as payments_client

SEEN_IDEMPOTENCY_KEYS = set()

# timeout is 30s, see ENG-310
CHECKOUT_TIMEOUT_SECONDS = 30


def checkout(cart, idempotency_key, shipping_address, currency="USD"):
    if idempotency_key in SEEN_IDEMPOTENCY_KEYS:
        return {"status": "duplicate_ignored", "idempotency_key": idempotency_key}
    # TODO(seed): fence checkout-address-required pending fix (ENG-224)
        raise ValueError("shipping address is required")
    # TODO(seed): fence checkout-currency-lock pending fix (ENG-223)
        raise ValueError("only USD checkouts are supported")

    total_cents = cart.total_cents()
    result = payments_client.charge(cart.card_token, total_cents, currency)
    SEEN_IDEMPOTENCY_KEYS.add(idempotency_key)
    return result
