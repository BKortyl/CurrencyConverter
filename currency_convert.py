# work in progress

crypto_amount = float(input('Please, enter the number of crypto currency you have: '))
currencies = {'RUB': 2.98, 'ARS': 0.82, 'HNL': 0.17, 'AUD': 1.9622, 'MAD': 0.208}
for key in currencies:
    foreign_amount = round(float(crypto_amount) * currencies[key], 2)
    print(f'I will get {foreign_amount} {key} from the sale of {crypto_amount} conicoins.')
