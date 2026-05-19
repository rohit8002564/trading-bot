"""Command-line interface entry point."""

import argparse

from bot.orders import place_order
from bot.validators import validate_side, validate_order_type, validate_quantity


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:

        # Validation layer
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        price = float(args.price) if args.price else None

        if order_type == "LIMIT" and price is None:
            raise ValueError("Price is required for LIMIT orders")

        # Request summary
        print("\n===== ORDER REQUEST =====")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price is not None:
            print(f"Price: {price}")

        # Place order
        response = place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        # Response output
        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")

        print("\nOrder placed successfully!")

    except Exception as e:
        print(f"\nError: {str(e)}")


if __name__ == "__main__":
    main()