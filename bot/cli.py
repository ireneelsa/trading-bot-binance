import argparse
import sys
from bot.orders import OrderManager
from bot.validators import validate_order_input

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet CLI Trader")
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--qty", required=True, type=float, help="Quantity to trade")
    parser.add_argument("--price", required=False, type=float, help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    # Step 1: Validation
    try:
        cleaned_inputs = validate_order_input(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.qty,
            price=args.price
        )
    except ValueError as ve:
        print(f"[ERROR] Invalid input: {ve}")
        sys.exit(1)
        
    symbol = cleaned_inputs["symbol"]
    side = cleaned_inputs["side"]
    order_type = cleaned_inputs["order_type"]
    quantity = cleaned_inputs["quantity"]
    price = cleaned_inputs["price"]

    price_str = price if price is not None else "N/A"

    # Step 2: Print order summary block
    print("==============================")
    print("  Trading Bot - Order Request ")
    print("==============================")
    print(f"  Symbol   : {symbol}")
    print(f"  Side     : {side}")
    print(f"  Type     : {order_type}")
    print(f"  Quantity : {quantity}")
    print(f"  Price    : {price_str}")
    print("==============================")

    # Step 3: Order placement
    try:
        manager = OrderManager()

        if order_type == "MARKET":
            manager.place_market_order(symbol=symbol, side=side, quantity=quantity)
        elif order_type == "LIMIT":
            manager.place_limit_order(symbol=symbol, side=side, quantity=quantity, price=price)
            
        print("[SUCCESS] Order placed successfully!")
    except Exception as e:
        print(f"[ERROR] Order failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
