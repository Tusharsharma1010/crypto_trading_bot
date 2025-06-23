🚀 Crypto Trading Bot – Binance Futures (Testnet)
This is a Python-based command-line trading bot that places orders on the Binance USDT-M Futures Testnet. The bot uses python-binance and supports Market, Limit, and Stop-Market order types. It securely loads your API credentials via a .env file and logs all transactions for review.

📦 Features
✅ Place BUY and SELL orders

✅ Support for Market, Limit, and Stop-Market orders

🔐 Secure API credentials via .env file

💬 Command-line interface for user input

🧾 Logs all API requests/responses in bot_logs.log

❌ Ignores sensitive files using .gitignore

🛠️ Setup
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/Tusharsharma1010/crypto_trading_bot.git
cd crypto_trading_bot
2. Install Dependencies
nginx
Copy
Edit
pip install -r requirements.txt
3. Create a .env File
In the root folder, create a .env file and add your Binance Testnet API credentials:

ini
Copy
Edit
API_KEY=your_api_key_here  
API_SECRET=your_api_secret_here
🚨 Do NOT upload .env to GitHub. It's ignored via .gitignore.

🚀 How to Run
nginx
Copy
Edit
python cli.py
You will be prompted like this:

pgsql
Copy
Edit
📈 Welcome to the Binance Futures Testnet Trading Bot
🔁 Enter trading symbol (e.g., BTCUSDT)
📊 Enter order side (BUY / SELL)
⚙️ Enter order type (MARKET / LIMIT / STOP_LIMIT)
📦 Enter quantity
⛔ Enter stop price (for STOP_LIMIT only)
💰 Enter limit price (for LIMIT or STOP_LIMIT orders)
🧾 Example
Market Order (Buy 0.01 BTCUSDT):

yaml
Copy
Edit
🔁 Enter trading symbol: BTCUSDT
📊 Enter order side: BUY
⚙️ Enter order type: MARKET
📦 Enter quantity: 0.01
📂 Project Structure
bash
Copy
Edit
crypto_trading_bot/
├── bot.py
├── cli.py
├── .env               # Not tracked (private)
├── .gitignore
├── README.md
├── requirements.txt
├── bot_logs.log
📜 License
This project is open-source under the MIT License.

🙋‍♂️ Author
Tushar Sharma
🔗 GitHub Profile

⚠️ For demo/testing purposes only. Not for real-money trading.
