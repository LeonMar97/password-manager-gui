from fastapi import FastAPI

app = FastAPI()

@app.get('/api/db')
def get_db():
    return {"hello":"yes"}
