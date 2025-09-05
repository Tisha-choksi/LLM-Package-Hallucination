import ccxt
import time

# Replace with your own API keys
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Initialize the exchange (e.g., Binance)
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

# Set the symbol and amount for trading
symbol = 'BTC/USDT'
amount = 0.001  # Adjust this to your preferred amount

def fetch_price():
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

def place_order(order_type='buy'):
    if order_type == 'buy':
        order = exchange.create_market_buy_order(symbol, amount)
    else:
        order = exchange.create_market_sell_order(symbol, amount)
    return order

if __name__ == "__main__":
    while True:
        try:
            price = fetch_price()
            print(f"Current price of {symbol}: {price} USDT")

            # Example condition to place a buy order
            if price < 30000:  # Example threshold
                print("Placing a buy order...")
                order = place_order('buy')
                print(f"Buy order placed: {order}")
            else:
                print("Price is too high for buying.")

            time.sleep(60)  # Wait for 1 minute before checking again

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)  # Wait before retrying
