# print('Простий калькулятор')
# while True:
#     num1 = (input('Введіть перше число:'))
#     if num1 == 'exit':
#         break
#     num1=float(num1)
#     op = input("Введіть операцію (+, -, *, /, **, //):")
#     if op == 'exit':
#         break
#     num2 = input("Введіть друге число:")
#     if num2 == "exit":
#         break
#     num2=float(num2)
#     if op == '+':
#         result = num1 + num2
#     elif op == '-':
#         result = num1 - num2
#     elif op == '*':
#              result = num1 * num2
#     elif op == '/':
#         if num2 != 0:
#             result = num1 / num2
#         if num2 == 0:
#             result = "Ділення на 0 неможливе!"
#     elif op == '**':
#         result = num1 ** num2
#     elif op == '//':
#         result = num1 // num2
#     else:
#         result = "Невідома операція!"
#     print("Результат:", result)

# name=input('Як Вас звати? ')
# age=int(input('Скільки Вам років? '))
# print('Привіт,',name,'!',"Через рік Вам буде", age+1, "років.")
#
# #
print("Конвертер температури")
c=float(input("Введіть значення температури за Цельсієм: "))
f=c*9/5+32
print("Результат: ",f,"градусів за Фаренгейтом" )