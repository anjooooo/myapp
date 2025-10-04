from fastapi import FastAPI, HTTPException
# from app.routes import router


# # 라우터 등록
# app.include_router(router)


app = FastAPI()

fake_users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.get("/")
def root():
    return {"massage": "Hello FastAPI!"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}

@app.get("/users")
def get_users():
    return {"users": fake_users}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in fake_users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/users")
def add_user(user: dict):
    new_id = len(fake_users) + 1
    user["id"] = new_id
    fake_users.append(user)
    return {"massage": "User added", "user": user}

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: dict):
    for user in fake_users:
        if user["id"] == user_id:
            user["name"] = updated_user["name"]
            return {"massage": "User updated", "user": user}
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for user in fake_users:
        if user["id"] == user_id:
            fake_users.remove(user)
            return {"massage": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@app.get("/error")
def trigger_error():
    raise HTTPException(status_code=500, detail="This is a simulated error")
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi import FastAPI
# from app.routes import router
# from app.database import engine, Base

