from fastapi import FastAPI, HTTPException, Depends, Cookie, Response
from pydantic import BaseModel, EmailStr
import asyncio
import uuid

app = FastAPI(
    title='Asyncronic API Server',
    description="Повна фігня!!!",
    version="1.0.0",
)

# =========================
# 🧠 Fake async database
# =========================

fake_users_db = {
    "user@example.com": {
        "password": "123456",
        "name": "Vova"
    },
    "user1@example.com": {
        "password": "1234567",
        "name": "Igor"
    }
}

fake_sessions_db = {}



async def fake_db_delay():
    # імітація затримки БД
    await asyncio.sleep(0.3)


# 📦 Schemas
# =========================

class RegisterSchema(BaseModel):
    email: EmailStr
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

# =========================
# 🔐 Auth helpers
# =========================

async def create_session(user_id: str) -> str:
    await fake_db_delay()
    session_id = str(uuid.uuid4())
    fake_sessions_db[session_id] = user_id
    return session_id

async def get_user_by_session(session_id: str):
    await fake_db_delay()
    user_id = fake_sessions_db.get(session_id)
    if not user_id:
        return None
    return fake_users_db.get(user_id)

# =========================
# 🧱 Dependencies
# =========================

async def get_current_user(
    session_id: str | None = Cookie(default=None)
):
    """
    Dependency:
    - читає session_id з cookie
    - шукає користувача
    - якщо нема → 401
    """
    if not session_id:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = await get_user_by_session(session_id)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid session")

    return user

# =========================
# 🚀 Endpoints
# =========================

@app.post("/register")
async def register(data: RegisterSchema):
    await fake_db_delay()

    if data.email in fake_users_db:
        raise HTTPException(status_code=400, detail="User already exists")

    fake_users_db[data.email] = {
        "id": data.email,
        "email": data.email,
        "password": data.password,  # ❗ у реальності хешувати
    }

    return {"message": "User registered"}

@app.post("/login")
async def login(data: LoginSchema, response: Response):
    await fake_db_delay()

    user = fake_users_db.get(data.email)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    session_id = await create_session(user["id"])

    # 🍪 Set cookie
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True
    )

    return {"message": "Logged in"}

@app.get("/me")
async def me(current_user=Depends(get_current_user)):
    """
    Protected endpoint
    """
    return {
        "email": current_user["email"]
    }
@app.get("/list_users")
async def list_users():
# async def all_users():
    return fake_users_db

@app.post("/logout")
async def logout(
    response: Response,
    session_id: str | None = Cookie(default=None)
):
    if session_id:
        fake_sessions_db.pop(session_id, None)

    response.delete_cookie("session_id")
    return {"message": "Logged out"}