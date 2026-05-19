# trading_bot1

---

# 📘 Binance Futures Testnet Trading Bot

## 📌 Overview

This is a simple Python CLI-based trading bot that interacts with the **Binance Futures Testnet (USDT-M)**.
It supports placing **MARKET** and **LIMIT** orders with proper validation, logging, and error handling.

---

## ⚙️ Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL sides
* CLI-based user input
* Input validation (side, type, quantity, price)
* Structured API client layer
* Logging of requests and responses
* Exception handling for API and input errors

---

## 📁 Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py          # Binance API client setup
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation functions
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # Command-line interface
├── logs/                  # Log files (generated automatically)
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🛠️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd trading_bot
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Setup Environment Variables

Create a `.env` file:

```env
BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret
```

---

## ▶️ How to Run

### 🔹 MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

### 🔹 LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

## 📤 Example Output

```
===== ORDER REQUEST =====
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

===== ORDER RESPONSE =====
Order ID: 123456789
Status: NEW
Executed Qty: 0.0000
Avg Price: 0.00

Order placed successfully!
```

---

## 📊 Logging

All API requests and responses are stored in:

```
logs/trading_bot.log
```

Logs include:

* Order request parameters
* API responses
* Errors and exceptions

---

## ⚠️ Assumptions

* User has a valid Binance Futures Testnet account
* API keys are correct and active
* Internet connection is available

---

## 📦 Requirements

```
python-binance
python-dotenv
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 🔒 Security Note

Never upload your `.env` file or API keys to GitHub.

---

## 👨‍💻 Author

Simple Python Trading Bot for Binance Futures Testnet assignment.

---



