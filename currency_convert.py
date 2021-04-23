# work in progress
import requests


def menu():
    while True:
        choice = input("'calc' for calculator, 'list' for a list of current exchange rates, 'quit' to quit: ")
        if choice == 'calc':
            calculate_exchange()
        elif choice == 'list':
            exchange_rates(cache_rates())
            # TODO: Consider rework to request single exchange rates as user needs them, instead of caching everything.
        elif choice == 'quit':
            quit()
        else:
            print('Wrong input')


def calculate_exchange():  # TODO: Doesn't work for PLN, predict and take care of possible errors.
    currency_in = input('Please enter the code of currency that you have: ')
    currency_amount = float(input('Please, enter the amount of currency you have: '))
    currency_out = input('Please enter the code of currency that you want to exchange to: ')
    request_in = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_in}/?format=json')
    data_in = request_in.json()
    request_out = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency_out}/?format=json')
    data_out = request_out.json()
    result = round(currency_amount * data_in['rates'][0]['mid'] / data_out['rates'][0]['mid'], 2)
    print(f'I will get {result} {currency_out.upper()} from the sale of {currency_amount} {currency_in.upper()}.')


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
        elif currency_code.upper() in cache:
            flagged_currency[currency_code.upper()] = cache[currency_code.upper()]
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
