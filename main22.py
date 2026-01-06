import random



# # повертає число 1–6
def roll_dice():
    return random.randint(1, 6)


# # # повертає випадкове ім’я зі списку
# def get_random_name():
#     names=["Петя", "Вася", "Коля", "Слава"]
#     return random.choice(names)


# # генерує випадковий пароль
def random_password(length):
    letters=['a', 'b', 'c', 'd', 'e', 'f','g','h','s','g','q','r','m','s','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    password=''
    for i in range(1,length):
        password+=random.choice(letters)+random.choice(numbers)
    return password

print(random_password(7))