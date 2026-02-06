
#uvicorn app:app --reload --port 8010 --host 0.0.0.0


from fastapi import FastAPI

app=FastAPI()


@app.get("/")

def root():
    return {"Hello": "World"}