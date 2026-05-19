from binance.client import Client
from dotenv import load_dotenv
import os
import time

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

print("API KEY:", API_KEY)
print("API SECRET:", API_SECRET)

client = Client(API_KEY, API_SECRET, testnet=True)

# Time sync fix
server_time = client.get_server_time()
client.timestamp_offset = server_time['serverTime'] - int(time.time() * 1000)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"