from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import List

app = FastAPI()

# Модель контакту
class Contact(BaseModel):
    name: str
    phone: str
    email: EmailStr  # автоматична валідація email

# "База даних" у пам’яті
contacts_db = {}
next_id = 1


@app.post("/contacts", response_model=dict)
def create_contact(contact: Contact):
    global next_id
    contacts_db[next_id] = contact
    next_id += 1
    return {"id": next_id - 1, "contact": contact}


@app.get("/contacts", response_model=List[dict])
def get_contacts():
    return [{"id": cid, "contact": contact} for cid, contact in contacts_db.items()]


@app.get("/contacts/{contact_id}", response_model=dict)
def get_contact(contact_id: int):
    if contact_id not in contacts_db:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"id": contact_id, "contact": contacts_db[contact_id]}


@app.delete("/contacts/{contact_id}", response_model=dict)
def delete_contact(contact_id: int):
    if contact_id not in contacts_db:
        raise HTTPException(status_code=404, detail="Contact not found")
    deleted = contacts_db.pop(contact_id)
    return {"deleted_id": contact_id, "contact": deleted}