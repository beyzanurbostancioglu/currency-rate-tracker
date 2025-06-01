# 💱 Currency Rate Tracker

A simple web-based application that fetches and displays real-time currency exchange rates using the [ExchangeRate-API](https://www.exchangerate-api.com).

---

## 🌍 Features

- Real-time exchange rates based on USD  
- Displays rates for popular currencies: EUR, GBP, TRY, JPY, BTC  
- Search for any currency code manually  
- Clean and user-friendly web interface using Flask  

---

## 🧰 Technologies Used

- Python 3.10+
- Flask
- requests
- HTML/CSS (Jinja2 for templating)

---

## 🚀 Getting Started

Follow these steps to run the project locally:
### 1. Clone the Repository

```bash
git clone https://github.com/beyzanurbostancioglu/currency-rate-tracker.git
cd currency-rate-tracker
```
## 2. Install Dependencies
If pip is available:

```bash
pip install Flask requests
```
## Or if pip is not recognized:
```bash
python -m pip install Flask requests
```
## 3. Run the Application
```bash
python app.py
```
Then open your browser and go to:
```bash
http://127.0.0.1:5000
```
### 📁 Project Structure
```bash
currency-rate-tracker/
├── app.py              # Flask web interface
├── tracker.py          # Console version of the rate tracker
├── templates/
│   └── index.html      # HTML template file
├── static/             # (optional) static files like custom CSS or images
└── README.md           # Project documentation
```
### Usage
On first load, it shows exchange rates for 5 predefined currencies.

You can enter any valid currency code (e.g., AUD, CHF, CAD) into the input
to get its latest rate vs USD.

### Notes
This app uses a development server (Flask) and is not intended for production use.

It depends on the free ExchangeRate-API(https://www.exchangerate-api.com/), which may have limitations or rate limits.

## Contributions
Contributions are welcome!
Feel free to fork the repo, open issues, or submit a pull request.






