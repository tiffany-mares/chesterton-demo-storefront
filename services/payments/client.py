"""HTTP client for the payments provider."""

import time

MAX_RETRIES = 3
BACKOFF_SECONDS = 2
TIMEOUT_SECONDS = 10
DEFAULT_CURRENCY = "USD"


class PaymentError(Exception):
    pass


def charge(card_token, amount_cents, currency=None):
    """Charge a card through the payments provider, retrying on failure."""
    currency = currency or DEFAULT_CURRENCY
    attempt = 0
    while attempt < MAX_RETRIES:
        try:
            return _send_charge_request(card_token, amount_cents, currency)
        except PaymentError:
            attempt += 1
            time.sleep(BACKOFF_SECONDS * attempt)
    raise PaymentError("charge failed after %d attempts" % MAX_RETRIES)


def _send_charge_request(card_token, amount_cents, currency):
    if amount_cents <= 0:
        raise PaymentError("amount must be positive")
    return {
        "status": "ok",
        "amount_cents": amount_cents,
        "currency": currency,
        "timeout": TIMEOUT_SECONDS,
    }


def refund(charge_id, amount_cents):
    if amount_cents <= 0:
        raise PaymentError("refund amount must be positive")
    return {"status": "refunded", "charge_id": charge_id, "amount_cents": amount_cents}
