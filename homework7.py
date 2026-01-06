import random

class User:
    def __init__(self, name, age, email, role):
        self.name = name
        self.age = age
        self.email = email
        self.role = role

# # #def __init__(self, allowed_actions):
#           self.allowed_actions = allowed_actions

    def info(self):
        print(f"{self.name}, ({self.age}) років, електронна пошта {self.email}")

    def has_access(self, action):
        return action in self.role

#     def has_access(self, action):
#         return action in self.ROLE_PERMISSIONS.get(self.role, set())
#
#     # @property
#     # def role(self):
#     #     return self._role
#     #
#     # @level.setter
#     # def role(self, value):
#     #     if value == "admin" or "manager" or "user":
#     #         raise ValueError("Такого рівня доступу не передбачено")
#     #     self._role = value



## # генерує випадковий пароль
    def  generate_password(length):
        letters=['a', 'b', 'c', 'd', 'e', 'f','g','h','s','g','q','r','m','s','z']
        numbers=['0','1','2','3','4','5','6','7','8','9']
        password=''
        for i in range(1,length):
            password+=random.choice(letters)+random.choice(numbers)
        return password

users = [
    User("Boss", 43, 'bdjed.gmail.com', 'admin'),
    User("Deputy", 36, 'dwehids.ukrnet', 'manager'),
    User("Worker", 30, 'regrfhj.yahoo', 'user'),
]

if role=="admin":
    while True:
      print("\n1 — Додати користувача")
      print("2 — Показати всіх")
      print("3 — Знайти за email")
      print("4 — Вихід")
      choice = input("Виберіть дію: ")
      if choice == "1":
            name = input("Ім'я: ")
            age = int(input("Вік: "))
            email = input("Email: ")
            role = input ("Рівень доступу: ")
            users.append(User(name, age, email,role))
            print("Користувача додано!")
      elif choice == "2":
            for u in users:
                u.info()
      elif choice == "3":
            email = input("Введіть email: ")
            found = False
            for u in users:
              if u.email == email:
                u.info()
                found = True
              if not found:
                print("Не знайдено!")
      elif choice == "4":
            break
      else:
           print("Некоректний вибір!")

if role=="manager":
    while True:
      print("\n1 — Додати користувача")
      print("2 — Показати всіх")
      print("3 — Вихід")
      choice = input("Виберіть дію: ")
      if choice == "1":
            name = input("Ім'я: ")
            age = int(input("Вік: "))
            email = input("Email: ")
            role = input ("Рівень доступу: ")
            users.append(User(name, age, email,role))
            print("Користувача додано!")
      elif choice == "2":
            for u in users:
                u.info()
      elif choice == "3":
            break
      else:
           print("Некоректний вибір!")
if role=="user":
    while True:
      print("\n1 - Показати всіх")
      print("2 — Вихід")
      choice = input("Виберіть дію: ")
      if choice == "1":
            for u in users:
                u.info()
      elif choice == "2":
            break
      else:
           print("Некоректний вибір!")
