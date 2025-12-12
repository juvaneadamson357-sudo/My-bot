import time
import random

print("🚀 Bot started. Printing signals every second...")

while True:
    # Simulate a market price
    price = random.randint(100, 200)
    
    # Dummy strategy: even = BUY, odd = SELL
    if price % 2 == 0:
        signal = "BUY"
    else:
        signal = "SELL"
    
    # Print the price and signal
    print(f"Price: {price} | Signal: {signal}")
    
    # Wait 1 second before next tick
    time.sleep(1)