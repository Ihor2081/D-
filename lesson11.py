# import json
#
# with open("data.json", "r", encoding="utf-8") as f:
#      data = json.load(f)
#      print(data)

# with open("data.json", "w", encoding="utf-8") as f:
#      json.dump(data, f, indent=4, ensure_ascii=False)


import json

# 1. Прочитати JSON-файл
with open("products.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Припустимо, що структура така:
# {
#   "products": [
#       {"name": "Телефон", "price": 1000},
#       {"name": "Ноутбук", "price": 2000}
#   ]
# }

# 2. Вивести назви товарів
print("Назви товарів:")
for product in data["products"]:
    print(product["name"])

# 3. Порахувати кількість товарів
count = len(data["products"])
print("\nКількість товарів:", count)

#
#
# import csv
#
# ages = []  # список для збору віку
# row_count = 0  # лічильник рядків
#
# with open("data.csv", "r", encoding="utf-8") as f:
#     reader = csv.DictReader(f)
#
#     for row in reader:
#         print(row)  # вивід кожного рядка
#         row_count += 1  # збільшити кількість рядків
#
#         # Припустимо, що колонка називається "age"
#         age = int(row["age"])
#         ages.append(age)
#
# # Середній вік
# average_age = sum(ages) / len(ages) if ages else 0
#
# # Мінімальний вік
# min_age = min(ages) if ages else None
#
# print("\nКількість рядків:", row_count)
# print("Середній вік:", average_age)
# print("Мінімальний вік:", min_age)
#
