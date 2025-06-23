# 🚀 Crypto Trading Bot – Binance Futures (Testnet)

A Python-based automated trading bot for Binance USDT-M Futures Testnet. Supports Market, Limit, and Stop-Market orders via an interactive CLI.

---

## 📦 Features

- 🔑 Secure API key handling using `.env`
- 💬 Interactive command-line interface (CLI)
- ✅ Place **Market**, **Limit**, and **Stop-Market** orders
- 📄 Logging of all API responses and errors (`bot_logs.log`)
- 🔧 Built with `python-binance` and `dotenv`
- 🛠️ Easily extendable for future order types (OCO, Grid, etc.)

---

## 📂 Project Structure

crypto_trading_bot/
├── bot.py # Core bot logic (place orders)
├── cli.py # CLI user interaction script
├── .env # (Not committed) Contains your Binance API credentials
├── .gitignore # Excludes sensitive files like .env
├── requirements.txt # All Python dependencies
├── bot_logs.log # Logged order responses & errors
├── README.md # You're reading it!

---

## 🔐 Environment Setup

Create a `.env` file in the root folder with:

API_KEY=your_api_key_here
API_SECRET=your_api_secret_here


> ⚠️ Never commit your `.env` file to GitHub!

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/your-username/crypto_trading_bot.git
cd crypto_trading_bot

# Install dependencies
pip install -r requirements.txt

🚀 Running the Bot
python cli.py

The bot will guide you with prompts like:

Trading symbol (e.g., BTCUSDT)

Order side (BUY or SELL)

Order type (MARKET, LIMIT, STOP_LIMIT)

Quantity

Stop/Limit price if needed

📘 Sample Order Log (bot_logs.log)
2025-06-23 20:01:23,488 - INFO - Order Placed: {'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': '0.01', ...}


🎯 Future Enhancements
Add support for OCO or TWAP orders

Simple Streamlit UI (optional)

Add account balance and trade history features

🧑‍💻 Author
Tushar Sharma
Python Developer | AI + Trading Enthusiast
📧 tusharsharma2228@email.com
✅ License
This project is for educational/demo purposes using Binance Futures Testnet. Do not use with real funds without proper validation.
