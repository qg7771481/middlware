from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from datetime import datetime
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI(title="Middleware Example")


class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        method = request.method
        url = str(request.url)
        print(f"[{current_time}] {method} запит на {url}")

        if "Header" not in request.headers:
            return JSONResponse(
                status_code=400,
                content={"detail": "Відсутній заголовок Header"}
            )

        response = await call_next(request)
        return response

app.add_middleware(CustomMiddleware)


@app.get("/hello", tags=["Тести"])
def say_hello():
    return {"message": "наверно"}


@app.get("/ping", tags=["Тести"])
def ping():
    return {"message": "322"}


@app.get("/secure", tags=["Тести"])
def secure_route():
    return {"message": "Безкоштовний анти вірус"}
