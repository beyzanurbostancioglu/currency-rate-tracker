from flask import Flask, render_template
from tracker import get_currency_rates

app = Flask(__name__)

@app.route('/')
def index():
    rates = get_currency_rates()
    return render_template("index.html", rates=rates)

if __name__ == '__main__':
    app.run(debug=True)
