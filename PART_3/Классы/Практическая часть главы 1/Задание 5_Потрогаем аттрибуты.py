class BankAccount:
    account_number = ""
    owner_name = ""
    balance = 0.0
    is_active = True
    transaction_count = 0

# TODO: Создай банковский счет
account = BankAccount()

# TODO: Настрой начальные значения:# account_number: "12345-67890"# owner_name: "Иван Иванов" # balance: 10000.0# is_active: True# transaction_count: 0
account.account_number = '12345-67890'
account.owner_name = 'Иван Иванов'
account.balance = 10000.0
account.is_active = True
account.transaction_count = 0

print("=== Начальное состояние ===")
print(f"Счет: {account.account_number}")
print(f"Владелец: {account.owner_name}")
print(f"Баланс: {account.balance}₽")
print(f"Активен: {account.is_active}")
print(f"Операций: {account.transaction_count}")


# 1. Пополнение на 5000₽
print("\n=== Пополнение счета ===")
if account.is_active:
    summ_in = 5000
    account.balance += summ_in
    account.transaction_count += 1
    print(f'Ваш баланс пополнен на {summ_in} рублей')
else:
    print('Ваш аккаунт заблокирован, пополнение невозможно!')


# 2. Реализуй Снятие 3000₽
print("\n=== Снятие средств ===")
if account.is_active:
    summ_out = 3000
    if account.balance >= summ_out:
        account.balance -= summ_out
        account.transaction_count += 1
        print(f'Списание {summ_out} рублей!')



# 3. Попытка снять 20000₽
print("\n=== Попытка снять большую сумму ===")

sum_out = 20000
if account.is_active:
    if account.balance < sum_out:
        print(f'Вы пытаетесь снять больше чем есть на вашем балансе! Баланс: {account.balance}, Запрашиваемая сумма: {sum_out}')


print("\n=== Итоговое состояние ===")
print(f"Баланс: {account.balance}₽")
print(f"Активен: {'Да' if account.is_active else 'Нет'}")
print(f"Всего операций: {account.transaction_count}")