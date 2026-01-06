"""
Повний навчальний приклад FastAPI
Тема: Авторизація через Cookies + Swagger

✔ GET / POST
✔ Body (Pydantic)
✔ Cookies
✔ Depends
✔ Swagger Authorize

Файл можна запускати напряму:
    uvicorn exampleLogin:app --reload
"""

"""
Response — це один з найбільш “магічних” моментів FastAPI, який обовʼязково треба пояснити студентам.

Нижче — готовий блок конспекту + коментарі до коду, які можна прямо вставити в урок і в код.

🧩 Response — що це таке і навіщо він потрібен
📌 Що таке Response?

Response — це обʼєкт HTTP-відповіді, який FastAPI передає у ваш endpoint,
щоб ви могли керувати тим, що відправляється клієнту, окрім JSON-даних.

Якщо коротко:
Response = контроль над HTTP-відповіддю
"""

# ==============================
# ІМПОРТИ
# ==============================
from fastapi import FastAPI, Depends, HTTPException, Response
from fastapi.security import APIKeyCookie
from pydantic import BaseModel, EmailStr
import uuid

# ==============================
# ІНІЦІАЛІЗАЦІЯ ДОДАТКУ
# ==============================
app = FastAPI(
    title="FastAPI Cookie Auth Demo",
    description="Навчальний приклад авторизації через cookies",
    version="1.0.0"
)

# ==============================
# ТИМЧАСОВА "БАЗА ДАНИХ"
# (у реальному проєкті тут буде БД)
# ==============================

# Користувачі (email -> дані)
users_db = {
    "user@example.com": {
        "password": "123456",
        "name": "Vova"
    }
}

# Активні сесії (session_id -> email)
sessions: dict[str, str] = {}

# ==============================
# PYDANTIC-МОДЕЛІ
# ==============================

class LoginData(BaseModel):
    """
    Дані, які користувач надсилає при логіні
    Використовується як Body (JSON)
    """
    email: EmailStr
    password: str


class UserProfile(BaseModel):
    """
    Дані, які ми повертаємо у профілі
    """
    email: EmailStr
    name: str

# ==============================
# COOKIE SECURITY SCHEME
# ==============================

"""
APIKeyCookie:
- потрібен для Swagger
- додає кнопку Authorize
- дозволяє Swagger передавати cookie
"""

cookie_scheme = APIKeyCookie(name="session_id")

# ==============================
# ENDPOINT: LOGIN
# ==============================

@app.post("/login", summary="Login user and set cookie")
def login(data: LoginData, response: Response):
    """
    1. Приймаємо email + password (Body)
    2. Перевіряємо користувача
    3. Генеруємо session_id
    4. Записуємо session_id у cookie
    """

    # Шукаємо користувача
    user = users_db.get(data.email)

    # Якщо користувача немає або пароль неправильний
    if not user or user["password"] != data.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Генеруємо унікальний session_id
    session_id = str(uuid.uuid4())

    # Зберігаємо сесію
    sessions[session_id] = data.email

    # Встановлюємо cookie
    response.set_cookie(
        key="session_id",
        value=session_id,
        httponly=True  # cookie не доступна з JS
    )

    return {"message": "Logged is successfully"}

# ==============================
# ENDPOINT: PROFILE (PROTECTED)
# ==============================

@app.get(
    "/profile",
    response_model=UserProfile,
    summary="Get user profile (requires cookie)"
)
def profile(session_id: str = Depends(cookie_scheme)):
    """
    Захищений endpoint

    1. Читаємо session_id з cookie
    2. Перевіряємо, чи сесія існує
    3. Повертаємо дані користувача
    """

    # Отримуємо email по session_id
    email = sessions.get(session_id)

    # Якщо сесії немає
    if not email:
        raise HTTPException(
            status_code=401,
            detail="Not authorized"
        )

    user = users_db[email]

    return {
        "email": email,
        "name": user["name"]
    }

# ==============================
# ENDPOINT: LOGOUT
# ==============================

@app.post("/logout", summary="Logout user")
def logout(
    response: Response,
    session_id: str = Depends(cookie_scheme)
):
    """
    1. Видаляємо session з памʼяті
    2. Видаляємо cookie у браузері
    """

    sessions.pop(session_id, None)

    response.delete_cookie("session_id")

    return {"message": "Logged out"}

# ==============================
# ROOT ENDPOINT
# ==============================

@app.get("/")
def root():
    return {
        "message": "FastAPI Cookie Auth Demo",
        "endpoints": ["/login", "/profile", "/logout"]
    }

"""
==============================
ЯК ТЕСТУВАТИ У SWAGGER
==============================

1️⃣ Запустити сервер:
    uvicorn exampleLogin:app --reload

2️⃣ Відкрити:
    http://127.0.0.1:8000/docs

3️⃣ Виконати POST /login:
    {
      "email": "user@example.com",
      "password": "123456"
    }

4️⃣ Виконати GET /profile
    ✔ cookie вже передається автоматично

5️⃣ Виконати POST /logout

==============================
"""