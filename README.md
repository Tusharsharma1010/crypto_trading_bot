# 🚀 Crypto Trading Bot – Binance Futures (Testnet)

This is a Python-based command-line trading bot that places orders on the **Binance USDT-M Futures Testnet**. The bot uses `python-binance` and supports **Market**, **Limit**, and **Stop-Market** order types. It securely loads your API credentials via a `.env` file and logs all transactions for review.

---

## 📦 Features

- ✅ Place **BUY** and **SELL** orders
- ✅ Support for **Market**, **Limit**, and **Stop-Market** orders
- 🔐 Secure API credentials via `.env` file
- 💬 Command-line interface for user input
- 🧾 Logs all API requests/responses in `bot_logs.log`
- ❌ Ignores sensitive files using `.gitignore`

---

## 🛠️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/Tusharsharma1010/crypto_trading_bot.git
cd crypto_trading_bot

Install Dependencies
pip install -r requirements.txt

Create a .env File
In the root folder, create a .env file and add your Binance Testnet API credentials:
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here

🚀 How to Run
python cli.py

You will be prompted like this:
📈 Welcome to the Binance Futures Testnet Trading Bot
🔁 Enter trading symbol (e.g., BTCUSDT)
📊 Enter order side (BUY / SELL)
⚙️ Enter order type (MARKET / LIMIT / STOP_LIMIT)
📦 Enter quantity
⛔ Enter stop price (for STOP_LIMIT only)
💰 Enter limit price (for LIMIT or STOP_LIMIT orders)

🧾 Example
Market Order (Buy 0.01 BTCUSDT):
🔁 Enter trading symbol: BTCUSDT
📊 Enter order side: BUY
⚙️ Enter order type: MARKET
📦 Enter quantity: 0.01

📂 Project Structure
crypto_trading_bot/
├── bot.py             # Bot logic and order placement
├── cli.py             # CLI for user interaction
├── .env               # Your API keys (not uploaded)
├── .gitignore         # Ensures sensitive files are not tracked
├── README.md          # Project documentation
├── requirements.txt   # Python dependencies
├── bot_logs.log       # Log file for order status and errors

📜 License
This project is open-source under the MIT License.

🙋‍♂️ Author
Built by Tushar Sharma
🔗 GitHub Profile
