import requests

def get_currency_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    data = response.json()

    print("Full API response:")
    print(data)

    print("\nParsed Output:\n")
    print("💱 Currency Rates (Base: USD)\n")

    if 'rates' in data:
        rates = data['rates']
        for currency in ['EUR', 'GBP', 'TRY', 'JPY', 'BTC']:
            rate = rates.get(currency, "No data")
            print(f"1 USD = {rate} {currency}")
    else:
        print("Error fetching data:", data.get('error'))

if __name__ == "__main__":
    get_currency_rates()
