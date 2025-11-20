# Написать функцию convert_currency(amount, rate, from_currency="USD", to_currency="EUR"),
# которая конвертирует сумму amount из валюты from_currency в валюту to_currency,
# используя курс rate
# Функция должна возвращать конвертированную сумму


def convert_currency(amount, rate, from_currency="USD", to_currency="EUR"):
    print(f'For {amount} {from_currency} your receive', amount * rate, to_currency)


convert_currency(2051, 0.011, 'RUB', 'USD')
convert_currency(to_currency = 'USD',amount = 2, from_currency = 'BTC', rate = 105000)
convert_currency(amount = 2, rate = 105000, from_currency = 'BTC', to_currency = 'USD')