from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="To-Do App")

# CORS - веб-сайттан қолдану үшін
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Модельдер
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class Todo(TodoCreate):
    id: int
    completed: bool = False

# Хранилище
todo_db = []
current_id = 1

# GET - Барлық задачаларды көру
@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todo_db

# POST - Жаңа задача қосу
@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    global current_id
    new_todo = Todo(
        id=current_id,
        title=todo.title,
        description=todo.description,
        completed=False
    )
    todo_db.append(new_todo)
    current_id += 1
    return new_todo

# PUT - Задачаны орындау/орындалмау
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, completed: bool):
    for todo in todo_db:
        if todo.id == todo_id:
            todo.completed = completed
            return {"message": "Жаңартылды"}
    raise HTTPException(status_code=404, detail="Задача табылмады")

# DELETE - Бір задачаны өшіру
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_db):
        if todo.id == todo_id:
            del todo_db[index]
            return {"message": "Задача өшірілді"}
    raise HTTPException(status_code=404, detail="Задача табылмады")

# DELETE - Барлық задачаларды өшіру
@app.delete("/todos")
async def delete_all_todos():
    todo_db.clear()
    return {"message": "Барлық задачалар өшірілді"}

@app.get("/")
async def root():
    return {"message": "To-Do API жұмыс істейді! /docs ашыңыз"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)