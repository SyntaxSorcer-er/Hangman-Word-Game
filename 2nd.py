# 1. Hardcoded dictionary for stock prices
stock_prices = {
    "AAPL": 220.50,
    "GOOG": 140.75,
    "MSFT": 420.10,
    "AMZN": 185.30,
    "TSLA": 255.00
}

# Initialize total portfolio value
total_investment = 0.0
portfolio_details = []

print("Welcome to the Stock Portfolio Tracker! 📈")
print("Available stocks and their prices:")
for symbol, price in stock_prices.items():
    print(f"  - {symbol}: ${price}")

while True:
    # 2. Get user input for stock and quantity
    stock_symbol = input("\nEnter a stock symbol (e.g., AAPL) or type 'done' to finish: ").upper()

    if stock_symbol == 'DONE':
        break

    if stock_symbol not in stock_prices:
        print("Invalid stock symbol. Please try again.")
        continue

    try:
        quantity = int(input(f"Enter the quantity of {stock_symbol}: "))
        if quantity <= 0:
            print("Quantity must be a positive number.")
            continue
    except ValueError:
        print("Invalid quantity. Please enter a whole number.")
        continue

    # 3. Calculate value and update total
    price = stock_prices[stock_symbol]
    stock_value = price * quantity
    total_investment += stock_value

    # Store details for optional file save
    portfolio_details.append(f"{stock_symbol}: {quantity} shares at ${price} each. Total value: ${stock_value:.2f}")

    print(f"Added {quantity} shares of {stock_symbol}. Current total value: ${total_investment:.2f}")

# 4. Display total investment value
print(f"\nYour total portfolio investment is: ${total_investment:.2f}")

# 5. Optional: Save results to a file
save_option = input("Do you want to save your portfolio details to a file? (yes/no): ").lower()
if save_option == 'yes':
    file_name = "portfolio_summary.txt"
    try:
        with open(file_name, "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("-----------------------\n")
            for detail in portfolio_details:
                file.write(detail + "\n")
            file.write(f"\nTotal Portfolio Value: ${total_investment:.2f}\n")
        print(f"Portfolio summary successfully saved to {file_name} 🎉")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")