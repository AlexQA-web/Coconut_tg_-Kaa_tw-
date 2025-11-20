# Задание№2
# Конвертер валют Создайте класс CurrencyConverter с методами:
# usd_to_eur(amount): Конвертирует сумму в USD в EUR по курсу 0.85
# eur_to_usd(amount): Конвертирует сумму в EUR в USD по курсу 1.18

class CurrencyConverter:

    @staticmethod
    def usd_to_eur(amount):
        return amount * 0.85

    @staticmethod
    def eur_to_usd(amount):
        return amount * 1.18

print(CurrencyConverter.usd_to_eur(200))
print(CurrencyConverter.eur_to_usd(200))
