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

    try:
        # Validate inputs
        # validate_order_input raises ValueError if anything is invalid
        cleaned_inputs = validate_order_input(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.qty,
            price=args.price
        )
        
        # Extract validated/cleaned data
        symbol = cleaned_inputs["symbol"]
        side = cleaned_inputs["side"]
        order_type = cleaned_inputs["order_type"]
        quantity = cleaned_inputs["quantity"]
        price = cleaned_inputs["price"]

        # Initialize the order manager
        manager = OrderManager()

        # Route the order to the correct method based on order_type
        if order_type == "MARKET":
            manager.place_market_order(symbol=symbol, side=side, quantity=quantity)
        elif order_type == "LIMIT":
            manager.place_limit_order(symbol=symbol, side=side, quantity=quantity, price=price)
            
    except ValueError as ve:
        # Validation error from validate_order_input()
        print(f"Validation Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected exceptions (e.g., connection errors from place_order)
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
