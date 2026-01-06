# class Email:
#     def __init__(self,email):
#         self.email=email

import re

class InvalidEmailError(Exception):
    pass
class EmptyFieldError(Exception):
    pass
class OutOfStockError(Exception):
    pass

def get_valid_email():
    pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'

    while True:
        email = input("Введіть електронну пошту: ").strip()
        try:

            if not re.match(pattern, email):
                raise InvalidEmailError(f"Невірний формат e-mail {email}")
            print("E-mail валідний!")
            return email

        except InvalidEmailError:
            print("Невірний формат e-mail. Спробуйте ще раз")

def login_system():
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not username:
        raise EmptyFieldError("Поле 'username' не може бути порожнім!")

    if not password:
        raise EmptyFieldError("Поле 'password' не може бути порожнім!")

    print("Успішний вхід!")
    return username, password

def shop():
    items = {
        "apple": 10,
        "banana": 5,
        "milk": 3
    }

    print("\nДоступні товари:")
    for item, qty in items.items():
        print(f"{item}: {qty}")

    product = input("\nЩо хочете купити? ").strip().lower()

    if product not in items:
        raise ValueError("Невідомий товар!")

    try:
        amount = int(input("Скільки одиниць?: ").strip())
    except ValueError:
        raise ValueError("Потрібно вводити число!")

    if amount <= 0:
        raise ValueError("Кількість має бути > 0!")

    if amount > items[product]:
        raise OutOfStockError("Недостатньо товару на складі!")

    items[product] -= amount
    print(f"Ви успішно купили {amount} шт. {product}. Залишок: {items[product]}")

# ------------------------- MAIN -------------------------
try:
    print("=== Перевірка e-mail ===")
    email = get_valid_email()
    print("Ваш e-mail прийнято!\n")

    print("=== Login System ===")
    login_system()
    print()

    print("=== Магазин ===")
    shop()

except (InvalidEmailError, EmptyFieldError, OutOfStockError, ValueError) as e:
    print(f"\nПомилка: {e}")

except Exception as e:
    print(f"\nНепередбачена помилка: {e}")
