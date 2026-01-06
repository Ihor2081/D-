# print("Перевірка числа на парність")
# a=int(input("Введіть число: "))
# if a%2==0:
#     print("Введене число є парним")
# else:
#     print("Введене число є непарним")

# a=4728
# code=int(input("Введіть цифровий пароль: "))
# if code==a:
#     print("Доступ дозволено")
# else:
#     print("Ви ввели неправильний пароль")
# print(f'Правильний пароль - {a}')

# import random
# secret=random.randint(1,10)
#
# attempts = 3
# for attempt in range(attempts):
#         try:
#             guess = int(input("Вгадайте число від 1 до 10: "))
#         except ValueError:
#             print("Будь ласка, введіть ціле число.")
#             continue
#
#         if guess==secret:
#           print("Вітаю! Ви вгадали!")
#           break
#         elif guess>secret:
#           print("Забагато!")
#         else:
#           print("Замало!")
#
# print(f"На жаль, у вас закінчилися спроби. Загадане число було {secret}.")

# def is_even(n):
#     """Повертає True, якщо число парне"""
#     if n%2==0:
#         return True
#     else:
#         return False
# print(is_even(10))

# def sum_list(numbers):
#     sum=0
#     for i in numbers:
#         sum+=i
#     return sum
# print(sum_list([1,2,3,4,5]))

# def reverse_string(text):
#     return text[::-1]
# print(reverse_string("Привіт"))

# def count_vowels(word):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     count = 0
#     for letter in word:
#         if letter in vowels:
#             count += 1
#     return count
#
# print(count_vowels("gamechanger"))
