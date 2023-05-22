from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class MyRequestSchema(BaseModel):
    url: str


class MyResponseSchema(BaseModel):
    response: str


def my_inference_fn(req: MyRequestSchema) -> MyResponseSchema:
    # This is an example inference function - you can instead import a function from your own codebase,
    # or shell out to the OS, etc.
    resp = req.url + "_hello"
    return MyResponseSchema(response=resp)


@app.post("/predict")
async def predict(request: MyRequestSchema) -> MyResponseSchema:
    response = my_inference_fn(request)
    return response


@app.get("/readyz")
def readyz():
    return "ok"