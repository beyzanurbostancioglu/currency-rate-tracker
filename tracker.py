import requests

def get_currency_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    data = response.json()

    if 'rates' in data:
        rates = data['rates']
        selected_currencies = ['EUR', 'GBP', 'TRY', 'JPY', 'BTC']
        filtered_rates = {currency: rates.get(currency, "No data") for currency in selected_currencies}
        return {
            "base": data.get("base_code", "USD"),
            "rates": filtered_rates
        }
    else:
        return {
            "base": "USD",
            "rates": {},
            "error": data.get('error', 'Unknown error')
        }

if __name__ == "__main__":
    result = get_currency_rates()

    print("💱 Currency Rates (Base: {})\n".format(result["base"]))

    for currency, rate in result["rates"].items():
        print(f"1 {result['base']} = {rate} {currency}")
