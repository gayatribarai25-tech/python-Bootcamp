from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Learn FastAPI", "completed": False},
    {"id": 3, "title": "Practice SQL", "completed": True}
]


class TaskUpdate(BaseModel):
    title: str
    completed: bool


# Find task by ID
def find_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


# GET all tasks
@app.get("/tasks")
def get_tasks():
    return tasks


# GET one task
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return find_task(task_id)


# PUT update task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskUpdate):
    task = find_task(task_id)

    task["title"] = updated_task.title
    task["completed"] = updated_task.completed

    return {
        "message": "Task updated successfully",
        "task": task
    }


# DELETE task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    task = find_task(task_id)

    tasks.remove(task)

    return {"message": "Task deleted successfully"}