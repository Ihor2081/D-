# from fastapi import FastAPI
# # Імпортуємо клас FastAPI.
# # Це основний "фреймворк", за допомогою якого ми створюємо наш сервер та маршрути.
# app = FastAPI()
# # Створюємо об’єкт додатку.
# # Це — серце нашого API.
# # Саме в "app" ми будемо реєструвати всі маршрути (endpoint-и),
# # наприклад: /users, /products, /login, /items/{id} і т.д
# @app.get("/")
# def hello():
#     return {"message": "Hello FastAPI!"}
#
# @app.get("/users/{user_id}")
# def get_user(user_id: int):
#     return {"id": user_id}
#
# @app.get("/search")
# def search(q: str = None):
#     return {"query": q}
#
# from pydantic import BaseModel
# class Todo(BaseModel):
#     title: str
#     is_done: bool = False
#
# todos = []
# @app.post("/todos")
# def create(todo: Todo):
#   todos.append(todo)
#   return {"status": "created", "todo": todo}
#
# @app.get("/todos")
# def get_all():
#     return todos
#
# @app.get("/todos/{todo_id}")
# def get_one(todo_id: int):
#    if todo_id >= len(todos):
#      return {"error": "Not found"}
#    return todos[todo_id]
#
# # @app.delete("/todos/{todo_id}")
# # def delete(todo_id: int):
# #   if todo_id >= len(todos):
# #      return {"error": "Not found"}
# #   todos.pop(todo_id)
# #     return {"status": "deleted"}
# #
# # from tkinter.tix import Form
# from fastapi import FastAPI, HTTPException, Form
# from pydantic import BaseModel, EmailStr, Field
# from typing import Optional
#
# app = FastAPI()

# # ----- Модель для контакту -----
# class Contact(BaseModel):
#     name: str
#     phone: str
#     email: EmailStr   # автоматична валідація email
#
#
# # Тимчасова "база даних" у пам'яті
# contacts = []
# next_id = 1
#
#
# # ----- Створити контакт -----
# @app.post("/contacts")
# def create_contact(contact: Contact):
#     global next_id
#
#     new_contact = {
#         "id": next_id,
#         "name": contact.name,
#         "phone": contact.phone,
#         "email": contact.email
#     }
#
#     contacts.append(new_contact)
#     next_id += 1
#     return new_contact
#
#
# # ----- Отримати всі контакти -----
# @app.get("/contacts")
# def get_contacts():
#     return contacts
#
#
# # ----- Отримати контакт за ID -----
# @app.get("/contacts/{contact_id}")
# def get_contact(contact_id: int):
#     for c in contacts:
#         if c["id"] == contact_id:
#             return c
#     raise HTTPException(status_code=404, detail="Contact not found")
#
#
# # ----- Видалити контакт -----
# @app.delete("/contacts/{contact_id}")
# def delete_contact(contact_id: int):
#     for c in contacts:
#         if c["id"] == contact_id:
#             contacts.remove(c)
#             return {"message": "Contact deleted"}
#     raise HTTPException(status_code=404, detail="Contact not found")
#
# class Register(BaseModel):
#     username: str
#     email: EmailStr
#     age: Optional[int] = None
#     password: str = Field(min_length=8, max_length=64)
#
# @app.post("/register", response_model=Register)
# def register(
#     username: str = Form(...),
#     email: EmailStr = Form(...)
# ):
#     return {"username": username, "email": email}

# import asyncio
#
# async def print_data():
#     await asyncio.sleep(10)
#     return "Hello World!!"
#
# print(asyncio.run(print_data()))
