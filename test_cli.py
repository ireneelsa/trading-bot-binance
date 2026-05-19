import sys
import time
from bot import cli

def main():
    print("--- Test 1 ---")
    sys.argv = ["cli.py", "--symbol", "BTCUSDT", "--side", "BUY",
                "--type", "MARKET", "--qty", "0.001"]
    try:
        cli.main()
    except SystemExit as e:
        print(f"Test 1 exited with code {e}")
        
    print("\nWaiting 2 seconds...")
    time.sleep(2)

    print("\n--- Test 2 ---")
    sys.argv = ["cli.py", "--symbol", "BTCUSDT", "--side", "BUY",
                "--type", "LIMIT", "--qty", "0.001", "--price", "50000"]
    try:
        cli.main()
    except SystemExit as e:
        print(f"Test 2 exited with code {e}")

    print("\n--- Test 3 ---")
    sys.argv = ["cli.py", "--symbol", "BTCUSDT", "--side", "HOLD",
                "--type", "MARKET", "--qty", "0.001"]
    try:
        cli.main()
    except SystemExit as e:
        print(f"Caught expected SystemExit in Test 3: {e}")

    print("\n--- Test 4 ---")
    sys.argv = ["cli.py", "--symbol", "BTCUSDT", "--side", "BUY",
                "--type", "LIMIT", "--qty", "0.001"]
    try:
        cli.main()
    except SystemExit as e:
        print(f"Caught expected SystemExit in Test 4: {e}")

if __name__ == "__main__":
    main()
