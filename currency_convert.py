import requests


def menu():
    while True:
        choice = input("'calc' - calculator, 'list' - list of current exchange rates, 'tea' - faves, 'quit' - quit: ")
        if choice == 'calc':
            calculate_exchange(cache_rates())
        elif choice == 'list':
            exchange_rates(cache_rates())
        elif choice == 'tea':
            tea_currency_list(cache_rates())
        elif choice == 'quit':
            quit()
        else:
            print('Wrong input')


def calculate_exchange(cache):
    currency_in = input("Please enter the code of currency that you have, 'quit' to quit: ")
    if currency_in == 'quit':
        quit()
    elif currency_in.upper() == 'PLN':
        currency_in_rate = 1
    elif currency_in.upper() not in cache:
        print('Wrong input.')
        calculate_exchange(cache)
    else:
        currency_in_rate = cache[currency_in.upper()]

    currency_amount = input("Please, enter the amount of currency you have, 'quit' to quit: ")
    if currency_amount == 'quit':
        quit()
    try:
        currency_amount = float(currency_amount)
    except ValueError:
        print('Wrong Input. Please enter a number.')
        calculate_exchange(cache)

    currency_out = input("Please enter the code of currency that you want to exchange to, 'quit' to quit: ")
    if currency_out == 'quit':
        quit()
    elif currency_out.upper() == currency_in.upper():
        print('Wrong input.')
        calculate_exchange(cache)
    elif currency_out.upper() == 'PLN':
        currency_out_rate = 1
    elif currency_out.upper() not in cache:
        print('Wrong input.')
        calculate_exchange(cache)
    else:
        currency_out_rate = cache[currency_out.upper()]
    result = round(currency_amount * currency_in_rate / currency_out_rate, 2)
    print(f'I will get {result} {currency_out.upper()} from the sale of {currency_amount} {currency_in.upper()}.')


def exchange_rates(cache):
    flagged_currency = {}
    while True:
        currency_code = input("Please enter the currency code, 'print' to print the list or 'quit' to quit: ")
        if currency_code == 'quit':
            quit()
        elif currency_code == 'print':
            if not flagged_currency:
                print('Please add a currency to the list first.')
                exchange_rates(cache)
            else:
                print('Current exchange rates:')
                for currency in flagged_currency:
                    print(f'1 {currency} : {round(flagged_currency[currency], 2):.2f} PLN')
        elif currency_code.upper() in cache:
            flagged_currency[currency_code.upper()] = cache[currency_code.upper()]
        else:
            print('Wrong input')


def tea_currency_list(cache):
    flagged_currency = {'USD': cache['USD'], 'EUR': cache['EUR'], 'GBP': cache['GBP'], 'JPY': cache['JPY'],
                        'TWD': cache['TWD'], 'HKD': cache['HKD'], 'CNY': cache['CNY'], 'MYR': cache['MYR']}
    for currency in flagged_currency:
        print(f'1 {currency} : {round(flagged_currency[currency], 2):.2f} PLN')


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


def main():
    menu()


if __name__ == '__main__':
    main()
