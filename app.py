from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_currency_rates():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    data = response.json()

    if data.get("result") == "success":
        return data['rates'], data.get("time_last_update_utc", "Unknown")
    else:
        return {}, "Error"

@app.route("/", methods=["GET", "POST"])
def index():
    rates, last_update = get_currency_rates()
    result = {}
    query = ""
    error_message = ""

    if request.method == "POST":
        query = request.form.get("currency_code", "").upper()
        if query in rates:
            result[query] = rates[query]
        else:
            error_message = f"Currency code '{query}' not found."
    else:
        for code in ['EUR', 'GBP', 'TRY', 'JPY', 'BTC']:
            result[code] = rates.get(code, "No data")

    return render_template("index.html", rates=result, last_update=last_update, query=query, error=error_message)
if __name__ == "__main__":
    app.run(debug=True)
