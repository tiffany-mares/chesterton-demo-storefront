"""Shared helpers used across checkout, payments and inventory."""

import time

MAX_SLEEP_SECONDS = 30


def sleep_with_cap(seconds):
    time.sleep(min(seconds, MAX_SLEEP_SECONDS))


def validate_idempotency_key(key):
    if len(key) < 16:
        raise ValueError("idempotency key must be at least 16 characters")
    return key
