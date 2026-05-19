"""Validation helpers for order data."""


def validate_side(side):
    """Validate BUY/SELL side."""

    if not isinstance(side, str):
        raise ValueError("Side must be a string (BUY or SELL)")

    side = side.strip().upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):
    """Validate order type (MARKET/LIMIT)."""

    if not isinstance(order_type, str):
        raise ValueError("Order type must be a string (MARKET or LIMIT)")

    order_type = order_type.strip().upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity):
    """Validate order quantity."""

    try:
        quantity = float(quantity)
    except (TypeError, ValueError):
        raise ValueError("Quantity must be a number")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    return quantity


def validate_price(price, order_type):
    """Validate price for LIMIT orders."""

    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValueError("Price is required for LIMIT orders")

        try:
            price = float(price)
        except (TypeError, ValueError):
            raise ValueError("Price must be a number")

        if price <= 0:
            raise ValueError("Price must be greater than 0")

        return price

    return None