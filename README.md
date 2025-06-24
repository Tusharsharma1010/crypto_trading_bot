# 🚀 Crypto Trading Bot – Binance Futures (Testnet)

A Python-based trading bot for the Binance USDT-M Futures Testnet.  
Supports Market, Limit, and Stop-Market orders via a secure, interactive command-line interface.

---

## 📌 Features

- ✅ **Place Buy/Sell orders** with user input  
- 🔒 **Secure API key management** using `.env`  
- 🛠️ **Order types supported:**
  - Market  
  - Limit  
  - Stop-Market (Stop-Limit logic)  
- 🧾 **Logging** via `bot_logs.log`  
- 📜 **Real-time CLI prompts**  
- 🚫 **Ignores sensitive files** using `.gitignore`  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Tusharsharma1010/crypto_trading_bot.git
cd crypto_trading_bot
```

## 🔧 2. Install Dependencies
```
pip install -r requirements.txt
```

3. Create a .env File
```
API_KEY=your_api_key_here  
API_SECRET=your_api_secret_here
```

▶️ How to Run
```
python cli.py
```
You'll be prompted to enter:

Trading symbol (e.g., BTCUSDT)

Order side (BUY or SELL)

Order type (MARKET, LIMIT, or STOP_LIMIT)

Quantity (e.g., 0.01)

(For STOP_LIMIT only) Stop Price and Limit Price

🧪 Example Usage
```
📈 Welcome to the Binance Futures Testnet Trading Bot
🔁 Enter trading symbol (e.g., BTCUSDT)
📊 Enter order side (BUY / SELL)
⚙️ Enter order type (MARKET / LIMIT / STOP_LIMIT)
📦 Enter quantity: 0.01
⛔ Enter stop price: 65000
💰 Enter limit price: 64900
```

🗂️ Project Structure
```
crypto_trading_bot/
├── bot.py             → Core order logic
├── cli.py             → CLI interaction script
├── .env               → Stores API credentials (not committed)
├── .gitignore         → Ignores .env and log files
├── README.md          → Project documentation
├── requirements.txt   → Dependencies
├── bot_logs.log       → Logs API responses/errors
```

📜 License
This project is open-source under the MIT License.

🧑‍💻 Author
Tushar Sharma
📎 GitHub Profile

⚠️ For demo/testing purposes only. Do not use on live trading without understanding the risks.
