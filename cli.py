from dotenv import load_dotenv
import os
from bot import BasicBot
from binance.enums import ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT

# Load API credentials from .env
load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

def main():
    print("📈 Welcome to the Binance Futures Testnet Trading Bot")
    bot = BasicBot(api_key, api_secret)

    while True:
        try:
            symbol = input("🔁 Enter trading symbol (e.g., BTCUSDT): ").strip()
            side = input("📊 Enter order side (BUY / SELL): ").strip().upper()
            order_type = input("⚙️ Enter order type (MARKET / LIMIT / STOP_LIMIT): ").strip().replace(" ", "_").upper()
            quantity = float(input("📦 Enter quantity: "))

            price = None
            stop_price = None

            if order_type == ORDER_TYPE_LIMIT:
                price = input("💰 Enter limit price: ").strip()

            elif order_type == "STOP_LIMIT":
                stop_price = input("⛔ Enter stop price: ").strip()
                # We do NOT ask for price here anymore

            # Place order with or without stop_price
            bot.place_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                order_type=order_type,
                price=price,
                stop_price=stop_price
            )

            cont = input("✅ Place another order? (yes/no): ").strip().lower()
            if cont != 'yes':
                print("👋 Exiting bot. Goodbye!")
                break

        except Exception as e:
            print(f"❗ Error: {e}")

if __name__ == "__main__":
    main()
