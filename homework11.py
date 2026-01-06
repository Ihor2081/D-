# import json
# import os
#
# FILENAME = "library.json"
#
# # --- Функції роботи з файлом ---
#
# def load_library():
#     """Завантаження JSON або створення нового."""
#     if not os.path.exists(FILENAME):
#         # Якщо файла нема — створюємо порожню бібліотеку
#         data = {"books": []}
#         save_library(data)
#         return data
#
#     with open(FILENAME, "r", encoding="utf-8") as f:
#         return json.load(f)
#
#
# def save_library(data):
#     """Збереження JSON у файл."""
#     with open(FILENAME, "w", encoding="utf-8") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
#
#
# # --- Логіка меню ---
#
# def add_book(data):
#     title = input("Введіть назву книги: ")
#     author = input("Введіть автора: ")
#     year = input("Рік видання: ")
#
#     book = {"title": title, "author": author, "year": int(year)}
#     data["books"].append(book)
#     print("Книгу додано!\n")
#
#
# def show_all(data):
#     print("\n--- Усі книги ---")
#     if not data["books"]:
#         print("Немає книг.\n")
#         return
#
#     for b in data["books"]:
#         print(f"{b['title']} — {b['author']} ({b['year']})")
#     print()
#
#
# def find_by_author(data):
#     author = input("Введіть автора: ")
#     print("\n--- Результати пошуку ---")
#
#     found = [b for b in data["books"] if b["author"].lower() == author.lower()]
#
#     if not found:
#         print("Книг цього автора не знайдено.\n")
#         return
#
#     for b in found:
#         print(f"{b['title']} — {b['author']} ({b['year']})")
#     print()
#
#
# def delete_book(data):
#     title = input("Введіть назву книги для видалення: ")
#
#     before = len(data["books"])
#     data["books"] = [b for b in data["books"] if b["title"].lower() != title.lower()]
#
#     if len(data["books"]) < before:
#         print("Книгу видалено!\n")
#     else:
#         print("Книги з такою назвою не знайдено.\n")
#
#
# # --- Головний цикл програми ---
#
# def main():
#     library = load_library()
#
#     while True:
#         print("=== МЕНЮ ===")
#         print("1 — Додати книгу")
#         print("2 — Показати всі")
#         print("3 — Знайти книгу за автором")
#         print("4 — Видалити книгу")
#         print("5 — Зберегти файл")
#         print("0 — Вихід")
#
#         choice = input("Ваш вибір: ")
#
#         if choice == "1":
#             add_book(library)
#         elif choice == "2":
#             show_all(library)
#         elif choice == "3":
#             find_by_author(library)
#         elif choice == "4":
#             delete_book(library)
#         elif choice == "5":
#             save_library(library)
#             print("Файл збережено!\n")
#         elif choice == "0":
#             save_library(library)
#             print("Вихід...")
#             break
#         else:
#             print("Невірний вибір!\n")
#
#
# if __name__ == "__main1__":
#     main()

import csv

students = []
grades = []


with open("students.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:
        name = row["name"]
        grade = float(row["grade"])  # оцінка

        students.append((name, grade))
        grades.append(grade)

# 1. Середній бал
average_grade = sum(grades) / len(grades) if grades else 0

# 2. Найуспішніший студент
best_student = max(students, key=lambda x: x[1]) if students else None

# 3. Кількість студентів
count_students = len(students)

print("Середній бал:", average_grade)
if best_student:
    print("Найуспішніший студент:", best_student[0], "—", best_student[1])
print("Кількість студентів:", count_students)