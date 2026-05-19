# Trading Bot - Binance Futures Testnet

## Overview
CLI app that places MARKET and LIMIT orders on Binance Futures Testnet (USDT-M). No real money involved.

## Requirements
- Python 3.x
- A free Binance Futures Testnet account (testnet.binancefuture.com)

## Setup
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root:
   ```env
   BINANCE_TESTNET_API_KEY=your_key_here
   BINANCE_TESTNET_API_SECRET=your_secret_here
   ```
4. Get free API keys from testnet.binancefuture.com (no credit card needed)

## How to Run

### Place a MARKET order
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --qty 0.001
```

### Place a LIMIT order
```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type LIMIT --qty 0.001 --price 50000
```

### Arguments
| Argument  | Required | Description                        |
|-----------|----------|------------------------------------|
| `--symbol`| Yes      | Trading pair e.g. BTCUSDT          |
| `--side`  | Yes      | BUY or SELL                        |
| `--type`  | Yes      | MARKET or LIMIT                    |
| `--qty`   | Yes      | Order quantity e.g. 0.001          |
| `--price` | No       | Required only for LIMIT orders     |

## Project Structure
```text
trading_bot/
  bot/
    __init__.py
    client.py         # Binance client wrapper
    orders.py         # Order placement logic
    validators.py     # Input validation
    logging_config.py # Logging setup
    cli.py            # CLI entry point
  README.md
  requirements.txt
  .env               # Not committed - contains API keys
```

## Logging
All API requests, responses, and errors are logged to `bot.log` in the project root.

## Assumptions
- Only USDT-M Futures testnet is supported
- Minimum order quantity for BTCUSDT is 0.001
- LIMIT orders use GTC (Good Till Cancelled) by default
- API keys are stored in `.env` and never committed to version control
