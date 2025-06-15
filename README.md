# 💹 Quotex CHF/JPY Signal Bot 📈

A powerful **Telegram bot** that delivers **real-time Quotex trading signals** for the **CHF/JPY (Swiss Franc / Japanese Yen)** currency pair using technical analysis (RSI + EMA) and market data from Twelve Data API.

---

## 🚀 Features

- 🔍 **Live CHF/JPY Price Feed**
- 🧠 **Technical Analysis** using RSI and EMA
- 📡 **Real-time Trade Signals** (Buy / Sell)
- ⚠️ **Signal Clarity Warnings** when market is indecisive
- 🤖 Fast, simple Telegram interaction with `/signal`
- 🔐 Secured API key handling via `.env` and `python-dotenv`

---

## 🛠️ Tech Stack

| Tool        | Purpose                        |
|-------------|--------------------------------|
| Python      | Core programming language      |
| Telegram API| Bot interface                  |
| Twelve Data | Real-time forex price feed     |
| `ta` lib    | Technical indicators (RSI/EMA) |
| `python-dotenv` | Secure config loading     |

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/quotex-chfjpy-bot.git
cd quotex-chfjpy-bot
python -m venv env
source env/bin/activate  # Or `env\Scripts\activate` on Windows
pip install -r requirements.txt
```

---

## 🔐 Setup Secrets

Create a `.env` file in the project root directory:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TWELVE_DATA_API_KEY=your_twelve_data_api_key
```

Then ensure `.env` is ignored by Git:

```bash
echo ".env" >> .gitignore
```

---

## ✅ Usage

Start the bot:

```bash
python bot.py
```

In Telegram, send the `/signal` command:

```
📈 CHF/JPY: 165.927
🔼 BUY Signal: RSI Oversold + Price above EMA
```

---

## 🧠 Strategy Logic

Signal detection uses:

- **RSI (Relative Strength Index)**: To identify overbought or oversold levels
- **EMA (Exponential Moving Average)**: To spot price trend direction

Signal logic:

- ✅ **BUY** when RSI < 30 and price > EMA
- ✅ **SELL** when RSI > 70 and price < EMA
- ❌ Otherwise: No signal is returned

---

## 📅 Coming Soon

- 🔔 Automatic scheduled signal alerts (every X minutes)
- 📰 Economic news + sentiment tracking
- 💰 Monetization features (paid VIP signals)
- 📊 Web dashboard (React + Django backend)

---

## 🙌 Contributing

Contributions are welcome!  
Please open an issue to suggest changes or improvements.

---

## 📄 License

MIT License © 2025 CONSCIENCE EKHOMWANDOLOR

---

## ☕ Credits

Built with ❤️ by AVT CONSCIENCE  
📊 Data from [Twelve Data](https://twelvedata.com)  
🤖 Bot powered by [Telegram Bot API](https://core.telegram.org/bots)

---
