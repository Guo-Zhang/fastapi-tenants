from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
def root(request: Request):
    return {"Host": request.headers["host"]}
