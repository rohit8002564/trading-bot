"""Order handling utilities."""

from binance.exceptions import BinanceAPIException
from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        # Add LIMIT order parameters
        if order_type.upper() == "LIMIT":

            if price is None:
                raise ValueError("Price is required for LIMIT orders")

            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Order Request: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Order Response: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e.message}")
        raise

    except ValueError as e:

        logger.error(f"Validation Error: {str(e)}")
        raise

    except Exception as e:

        logger.error(f"Unexpected Error: {str(e)}")
        raise