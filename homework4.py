# Напиши функцію, яка приймає речення і повертає його з великої літери.

# def capitalize_words(sentence):
#     words = sentence.split()
#     capitalized=[word.capitalize() for word in words]
#     return ' '.join(capitalized)
# print(capitalize_words('i love python'))

# Напиши функцію, яка замінює всі пробіли на дефіси.

# def defis_replace(sentence):
#     return sentence.replace(" ","-")
# print(defis_replace("Ми любимо Python"))

# # Напиши функцію, яка підраховує, скільки разів певне слово зустрічається у тексті.
# def count_word_in_text(text, word):
#     words = text.lower().split()
#     return  words.count(word)
#
# print(count_word_in_text("У мене є собака по кличці Шерлок. Собака завжди зустрічає мене після школи. Собака полюбляє гратися з м’ячем", "собака"))
#

# def word_frequency(text):
#     freq = {}
#     for word in text.lower().split():
#         freq[word] = freq.get(word, 0) + 1
#     return freq
# print(word_frequency('Собака, кіт, собака, собака, слон'))

# Створи функцію reverse_words(sentence), яка виводить слова у зворотному порядку.
# def reverse_words(sentense):
#     words = sentense.split()
#     rever=words[::-1]
#     return " ".join(rever)
#
# print(reverse_words("я люблю Python"))
