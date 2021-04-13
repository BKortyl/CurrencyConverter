# work in progress
import requests


currency_code = input('Please enter the currency code: ')
currency_amount = float(input('Please, enter the number of currency you have: '))
currencies = {1: 'usd', 2: 'eur'}
r = requests.get(f'http://www.floatrates.com/daily/{currency_code.lower()}.json')
data_json = r.json()
for item in currencies:
    foreign_amount = round(float(currency_amount) * data_json[currencies[item]]['rate'], 2)
    print(f'I will get {foreign_amount} {currencies[item].upper()} from the sale of {currency_amount} {currency_code.upper()}.')
