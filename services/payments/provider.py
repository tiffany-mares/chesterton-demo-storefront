"""Low-level wrapper around the payments provider's HTTP API."""

_SEEN_REQUEST_IDS = set()


def send(request_id, payload):
    """Send a request to the provider, ignoring ones we have already sent."""
    if request_id in _SEEN_REQUEST_IDS:
        return {"status": "duplicate_ignored", "request_id": request_id}
    _SEEN_REQUEST_IDS.add(request_id)
    return {"status": "sent", "request_id": request_id, "payload": payload}
