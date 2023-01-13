
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

from forex_python.converter import CurrencyRates
c = CurrencyRates()

# CURRENCIES = ["INR","USD", "CAD", "CNY", "DKK", "EUR"]

@app.route('/', methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
      try:
         amount = float(request.form['amount'])
         # amount = float(amount)
         from_c = request.form['from_c']
         to_c = request.form['to_c']
        
         result = c.convert(from_c, to_c, amount)
         return render_template('base.html',amount= amount, from_c = from_c, to_c = to_c, result=round(result, 2))
        
      except Exception as e:
         return '<h1>Bad Request : {}</h1>'.format(e)

    
   else:
      return render_template('base.html')

@app.route('/amount', methods=['GET'])
def amount():
   return render_template('amount.html')


if __name__ == "__main__":
    app.run(debug=True) #defUault port is 5000


# rom forex_python.converter import CurrencyRates
# c = CurrencyRates()
# from_currency = input("From Currency: ").upper()
# to_currency = input("To Currency: ").upper()
# print(from_currency, " To ", to_currency, amount)
# result = c.convert(from_currency, to_currency, amount)
# print(result)