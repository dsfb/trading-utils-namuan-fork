import os

from dotenv import load_dotenv

load_dotenv()

# Crypto
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")
EXCHANGE_API_SECRET = os.getenv("EXCHANGE_API_SECRET")
EXCHANGE = os.getenv("EXCHANGE")

# Telegram
GROUP_CHAT_ID = os.getenv("GROUP_CHAT_ID")

# Twitter
TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN_KEY = os.getenv("TWITTER_ACCESS_TOKEN_KEY")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

# Tradier
TRADIER_BASE_URL = "https://sandbox.tradier.com/v1"
TRADIER_TOKEN = os.getenv("TRADIER_TOKEN")
