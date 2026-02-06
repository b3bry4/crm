from fastapi import FastAPI

app = FastAPI()


users = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/users")
def create_user(user: str):
    users.append(user)
    return users