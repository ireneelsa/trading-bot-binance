import time
from bot import OrderManager

def main():
    print("Initializing OrderManager...")
    manager = OrderManager()

    # Test 1: MARKET BUY Order
    try:
        print("\n=== Testing MARKET BUY Order ===")
        manager.place_market_order(symbol="BTCUSDT", side="BUY", quantity=0.001)
    except Exception as e:
        print(f"MARKET order failed: {e}")

    print("\n--- waiting 2 seconds ---")
    time.sleep(2)

    # Test 2: LIMIT BUY Order
    try:
        print("\n=== Testing LIMIT BUY Order ===")
        manager.place_limit_order(symbol="BTCUSDT", side="BUY", quantity=0.001, price=50000.0)
    except Exception as e:
        print(f"LIMIT order failed: {e}")

    print("\nPhase 2 test complete")

if __name__ == "__main__":
    main()
