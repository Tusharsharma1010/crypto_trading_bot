# bot.py
import logging
from binance.client import Client
from binance.enums import (
    ORDER_TYPE_MARKET,
    ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC
)

# Define manually since it's missing from your version
ORDER_TYPE_STOP_MARKET = "STOP_MARKET"

from binance.exceptions import BinanceAPIException

# Setup logging
logging.basicConfig(
    filename='bot_logs.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'

    def place_order(self, symbol, side, quantity, order_type=ORDER_TYPE_MARKET, price=None, stop_price=None):
        try:
            symbol = symbol.upper()
            side = side.upper()

            order_params = {
                'symbol': symbol,
                'side': side,
                'quantity': quantity
            }

            if order_type == ORDER_TYPE_MARKET:
                order_params['type'] = ORDER_TYPE_MARKET

            elif order_type == ORDER_TYPE_LIMIT:
                order_params['type'] = ORDER_TYPE_LIMIT
                order_params['price'] = price
                order_params['timeInForce'] = TIME_IN_FORCE_GTC

            elif order_type == "STOP_LIMIT":
                order_params['type'] = ORDER_TYPE_STOP_MARKET
                order_params['stopPrice'] = stop_price
                order_params['timeInForce'] = TIME_IN_FORCE_GTC

            else:
                raise ValueError(f"Unsupported order type: {order_type}")

            order = self.client.futures_create_order(**order_params)
            logging.info(f"Order Placed: {order}")
            print("✅ Order executed successfully.")
            print(order)

        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
            print(f"❌ Binance API Error: {e}")
        except Exception as e:
            logging.error(f"General Error: {e}")
            print(f"❌ Unexpected Error: {e}")
