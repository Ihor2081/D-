from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import Optional, List
from datetime import datetime

# ==================================================
# 🔌 Database connection
# ==================================================

DATABASE_URL = "sqlite:///todos.db"

engine = create_engine(
    DATABASE_URL,
    echo=True  # показує SQL-запити (ДУЖЕ корисно для навчання)
)

def get_session():
    """
    Dependency:
    відкриває сесію БД
    і автоматично закриває її після запиту
    """
    with Session(engine) as session:
        yield session


# ==================================================
# 🧱 Database model (table)
# ==================================================

class Todo(SQLModel, table=True):
    """
    Це ТАБЛИЦЯ в базі даних
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    done: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)


# ==================================================
# 📦 Schemas (input data)
# ==================================================

class TodoCreate(SQLModel):
    """
    Дані, які приходять від клієнта при створенні
    """
    title: str
    description: Optional[str] = None


class TodoUpdate(SQLModel):
    """
    Дані для оновлення
    """
    done: bool


# ==================================================
# 🚀 FastAPI app
# ==================================================

app = FastAPI(title="Todo API with Database")


# ==================================================
# 🔨 Create tables on startup
# ==================================================

@app.on_event("startup")
def on_startup():
    """
    Створює таблиці при першому запуску
    (у продакшені роблять міграціями)
    """
    SQLModel.metadata.create_all(engine)


# ==================================================
# ➕ CREATE Todo
# ==================================================

@app.post("/todos", response_model=Todo)
def create_todo(
    todo: TodoCreate,
    session: Session = Depends(get_session)
):
    """
    Створення нової задачі
    """
    db_todo = Todo(**todo.dict())
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)  # отримуємо id з БД
    return db_todo


# ==================================================
# 📥 READ all Todos
# ==================================================

@app.get("/todos", response_model=List[Todo])
def get_todos(
    done: Optional[bool] = None,
    session: Session = Depends(get_session)
):
    """
    Отримати всі задачі
    Можна фільтрувати: ?done=true
    """
    statement = select(Todo)

    if done is not None:
        statement = statement.where(Todo.done == done)

    todos = session.exec(statement).all()
    return todos


# ==================================================
# 📥 READ one Todo
# ==================================================

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(
    todo_id: int,
    session: Session = Depends(get_session)
):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


# ==================================================
# ✏️ UPDATE Todo
# ==================================================

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(
    todo_id: int,
    data: TodoUpdate,
    session: Session = Depends(get_session)
):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.done = data.done
    session.commit()
    session.refresh(todo)
    return todo


# ==================================================
# ❌ DELETE Todo
# ==================================================

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    session: Session = Depends(get_session)
):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    session.delete(todo)
    session.commit()
    return {"message": "Todo deleted"}