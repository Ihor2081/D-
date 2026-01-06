# import math
# print(math.factorial(7))
#
# from datetime import datetime
#
# now = datetime.now()
# print(now)
# print(now.strftime("%d.%m.%Y %H:%M:%S"))

# class User:
#     # pass #пропустити помилку
#     name="Noname"
#     age=0
#     tel=7423920
#
# u=User()
# u2=User()
# u.name=678568899 #зміна атрибуту обєкта
#
# print(u.name, u.age, u.tel)
# print(u.age)
# print(u.tel)

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# u=User("Igor", 35)
# u2=User("Vova", 40)
# print(u.name, u.age)
# print(u2.name, u2.age)

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def print_data(self):
        print(self.name,",", self.age, self.email)

u=User(input("Введіть імя:"), input("Введіть вік: "), "werqp.gmail.com")
u2=User("ghgjh", 78, "798798")
u.print_data()
u2.print_data()
