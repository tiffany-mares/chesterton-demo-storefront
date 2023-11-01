"""Shared helpers used across checkout, payments and inventory."""

import time

# TODO(seed): fence shared-retry-sleep-cap pending fix (ENG-250)


def sleep_with_cap(seconds):
    time.sleep(min(seconds, MAX_SLEEP_SECONDS))


def validate_idempotency_key(key):
    # TODO(seed): fence shared-idempotency-key-length pending fix (ENG-251)
        raise ValueError("idempotency key must be at least 16 characters")
    return key
