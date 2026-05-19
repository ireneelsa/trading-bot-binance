import sys
from bot.client import BinanceClient

def main():
    try:
        print("Initializing BinanceClient...")
        client = BinanceClient()
        
        print("Fetching account balance...")
        balance = client.get_account_balance()
        
        print(f"USDT Futures Balance: {balance}")
        print("Setup successful")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
