# work in progress
import requests


def menu():
    while True:
        choice = input("'calc' for calculator, 'list' for a list of current exchange rates: ")
        if choice == 'calc':
            calculate_exchange()
        elif choice == 'list':
            exchange_rates(cache_rates())
            # TODO: Consider rework to request single exchange rates as user needs them, instead of caching everything.
        elif choice == 'quit':
            quit()
        else:
            print('Wrong input')


def calculate_exchange():  # TODO: Change to NBP API, rework to take currency which you want to get.
    currency_code = input('Please enter the currency code: ')
    currency_amount = float(input('Please, enter the amount of currency you have: '))
    currencies = {1: 'usd', 2: 'eur'}
    r = requests.get(f'http://www.floatrates.com/daily/{currency_code.lower()}.json')
    data_json = r.json()
    for item in currencies:
        foreign_amount = round(float(currency_amount) * data_json[currencies[item]]['rate'], 2)
        print(f'I will get {foreign_amount} {currencies[item].upper()} from the sale of {currency_amount} {currency_code.upper()}.')


def exchange_rates(cache):
    flagged_currency = {}
    while True:
        currency_code = input("Please enter the currency code, 'print' to print the list or 'quit' to quit: ")
        if currency_code == 'quit':
            quit()
        elif currency_code == 'print':
            print('Current exchange rates:')
            for currency in flagged_currency:
                print(f'1 {currency} : {round(flagged_currency[currency], 2)} PLN')
        elif currency_code in cache:
            flagged_currency[currency_code] = cache[currency_code]
        else:
            print('Wrong input')


def cache_rates():
    cache = {}
    request_a = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/?format=json')
    table_a_json = request_a.json()
    request_b = requests.get('http://api.nbp.pl/api/exchangerates/tables/B/?format=json')
    table_b_json = request_b.json()
    for currency in table_a_json[0]['rates']:
        cache[currency['code']] = currency['mid']
    for currency in table_b_json[0]['rates']:
        cache[currency['code']] = currency['mid']
    return cache


menu()
