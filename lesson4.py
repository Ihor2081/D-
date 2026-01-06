# def add(a, b):
#     """Повертає суму двох чисел."""
#     return a + b
# print(add.__doc__)
# print(add(3,9))

# text = "abanana"
# fruits = text.split('a')
# print(fruits)  # ['яблуко', 'груша', 'банан']

# fruits = ["яблуко", "груша", "банан"]
# result = ", ".join(fruits)
# print(result)  # яблуко, груша, банан

# text = "   Привіт! "
# print(text.strip())  # "Привіт"

# text = "Я люблю JavaJava"
# new_text = text.replace("Java", "Python")
# print(new_text)  # Я люблю Python
#
# print("python".upper())  # PYTHON
# print("HELLO".lower())  # hello
#
# # t = "python"
# t[0] = t[0].upper()

# t = 'python'.capitalize()
# print(t)
#
# # name = 'Олександр'
# template = "Привіт, {0}! Твій бал: {1}"
# print(template.format("Олександр", 95))

# try:
#     n = int(input('This is n = '))
#
#     res = 10 / n
#
#     print(res)
# except ValueError:
#     print('Please enter a number')
# except ZeroDivisionError:
#     print('We cannot divide by zero')
# finally:
#     print('We can continue running this code')

def text_parser(text):
  vowels = "аеєиіїоуюяaeiou"
  words = text.split()
  num_words = len(words)
  num_chars = len(text)
  num_vowels = sum(1 for ch in text.lower() if ch in vowels)
  return f"""
Аналіз тексту:
Слів: {num_words}
Символів: {num_chars}
Голосних: {num_vowels}
""

print(text_parser("Привіт, сьогодні гарна погода"))