from bot.client import BinanceClient
from bot.logging_config import setup_logger

logger = setup_logger("orders")

class OrderManager:
    def __init__(self):
        self.binance = BinanceClient()
        self.client = self.binance.get_client()

    def place_market_order(self, symbol: str, side: str, quantity: float) -> dict:
        try:
            logger.info(f"Preparing to place MARKET order: symbol={symbol}, side={side}, quantity={quantity}")
            
            if not self.client:
                raise Exception("Binance client is not initialized.")
                
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            
            logger.info(f"MARKET order response: {response}")
            
            print(f"Order Request: MARKET {side} {quantity} {symbol}")
            print(f"Order ID: {response.get('orderId')}")
            print(f"Status: {response.get('status')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            print(f"Avg Price: {response.get('avgPrice')}")
            print("Result: SUCCESS")
            
            return response
            
        except Exception as e:
            logger.error(f"Failed to place MARKET order: {e}")
            print(f"FAILED: {e}")
            raise

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> dict:
        try:
            logger.info(f"Preparing to place LIMIT order: symbol={symbol}, side={side}, quantity={quantity}, price={price}")
            
            if not self.client:
                raise Exception("Binance client is not initialized.")
                
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=str(price),
                timeInForce="GTC"
            )
            
            logger.info(f"LIMIT order response: {response}")
            
            print(f"Order Request: LIMIT {side} {quantity} {symbol} @ {price}")
            print(f"Order ID: {response.get('orderId')}")
            print(f"Status: {response.get('status')}")
            print(f"Executed Qty: {response.get('executedQty')}")
            print(f"Avg Price: {response.get('avgPrice')}")
            print("Result: SUCCESS")
            
            return response
            
        except Exception as e:
            logger.error(f"Failed to place LIMIT order: {e}")
            print(f"FAILED: {e}")
            raise
