print("Список покупок:")
shopping=[]

while True:

    action=input('Введіть дію(додати товар/видалити товар/показати список):')
    add = "додати товар"
    delete = "видалити товар"
    show = "показати список"
    if action == add:
        name = input("Введіть назву товару: ")
        shopping.append(name)
        print("Товар", name, "додано!")
    elif action==delete:
        name1=input("Введіть товар для видалення: ")
        if name1 in shopping:
            shopping.remove(name1)
            print("Товар", name1, "видалено")
        else:
            print("Такий товар у списку не виявлено!")
    elif action==show:
        print(shopping)
    elif action=="вихід":
        break

# print("Список контактів")
# contacts={}
#
# while True:
#     action=input('Введіть дію (add/delete/show/exit):')
#
#     if action=='add':
#         name=input("Введіть ім'я: ")
#         phone=input("Введіть номер телефону: ")
#         contacts[name]=phone
#     elif action=='show':
#         for name, phone in contacts.items():
#             print(f'{name}:{phone}')
#     elif action=='delete':
#         name=input("Введіть імя для видалення: ")
#         if name in contacts:
#             del contacts[name]
#             print("Контакт {name} видалено")
#         if name not in contacts:
#             print("Контакт не знайдено")
#     elif action=='exit':
#         print("До побачення!")
#         break
#     else:
#         print("Невідома команда")



