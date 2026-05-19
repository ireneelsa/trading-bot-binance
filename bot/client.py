import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from dotenv import load_dotenv
from bot.logging_config import setup_logger

# Load environment variables at the top
load_dotenv()

# Set up logger for the client
logger = setup_logger("client")

class BinanceClient:
    def __init__(self):
        self.api_key = os.getenv("BINANCE_TESTNET_API_KEY")
        self.api_secret = os.getenv("BINANCE_TESTNET_API_SECRET")
        
        if not self.api_key or not self.api_secret:
            logger.warning("BINANCE_TESTNET_API_KEY or BINANCE_TESTNET_API_SECRET is missing from environment variables.")

        try:
            # Initialize client with testnet=True
            self._client = Client(self.api_key, self.api_secret, testnet=True)
            
            # Explicitly enforce the required Base URL for futures
            self._client.API_URL = "https://testnet.binancefuture.com"
            self._client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
            self._client.FUTURES_TESTNET_URL = "https://testnet.binancefuture.com/fapi"
            
            logger.info("Binance Futures Testnet client initialized successfully.")
        except Exception as e:
            logger.error(f"Failed to initialize Binance Client: {e}")
            self._client = None

    def get_client(self) -> Client:
        """Returns the raw binance Client instance."""
        return self._client

    def get_account_balance(self) -> float:
        """Returns USDT balance from the futures account."""
        if not self._client:
            logger.error("Binance client is not initialized. Cannot fetch balance.")
            return 0.0
            
        try:
            # Fetch futures account info
            account_info = self._client.futures_account()
            
            # Search for USDT balance within the assets
            assets = account_info.get('assets', [])
            for asset in assets:
                if asset.get('asset') == 'USDT':
                    balance = float(asset.get('walletBalance', 0.0))
                    logger.debug(f"Successfully fetched USDT futures balance: {balance}")
                    return balance
            
            logger.warning("USDT asset not found in futures account balances.")
            return 0.0
            
        except (BinanceAPIException, BinanceRequestException) as e:
            logger.error(f"Connection/API error while fetching account balance: {e}")
            return 0.0
        except Exception as e:
            logger.error(f"Unexpected error while fetching account balance: {e}")
            return 0.0
