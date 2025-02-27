import requests
import pandas as pd
import matplotlib.pyplot as plt
API_KEY = 'your_alpha_vantage_api_key'

# Portfolio Dictionary
portfolio = {}

# Function to get real-time stock data
def get_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

# Function to add stock to portfolio
def add_stock(symbol, shares):
    data = get_stock_data(symbol)
    if 'Time Series (Daily)' in data:
        portfolio[symbol] = {'shares': shares, 'data': data['Time Series (Daily)']}
        print(f"{symbol} added to your portfolio with {shares} shares.")
    else:
        print(f"Failed to retrieve data for {symbol}.")

# Function to remove stock from portfolio
def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"{symbol} removed from your portfolio.")
    else:
        print(f"{symbol} is not in your portfolio.")

# Function to display portfolio
def display_portfolio():
    print("\nYour Portfolio:")
    for symbol, details in portfolio.items():
        print(f"{symbol}: {details['shares']} shares")
    print("\n")
# Function to track performance

def track_performance():
    for symbol, details in portfolio.items():
        data = details['data']
        dates = list(data.keys())
        close_prices = [float(data[date]['4. close']) for date in dates]

 # Plot stock performance
    plt.plot(dates, close_prices, label=symbol)
    plt.title('Stock Portfolio Performance')
    plt.xlabel('Date')
    plt.ylabel('Closing Price')
    plt.legend()
    plt.show()

 # Main menu function
def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Track Performance")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            remove_stock(symbol)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            track_performance()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ =="__main__":
             main()
