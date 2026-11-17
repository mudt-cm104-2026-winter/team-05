from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app import storage

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"entries": storage.all_entries()},
    )


@app.post("/calculate")
def calculate(
    num1: float = Form(...),
    op: str = Form(...),
    num2: Optional[float] = Form(None),
):
    if op == "%":
        if num2 is not None:
            result = (num1 / 100) * num2
        else:
            result = num1 / 100
            num2 = 100.0
    else:
        if num2 is None:
            return RedirectResponse(url="/", status_code=303)

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2 if num2 != 0 else "Error (division by zero)"
        else:
            return RedirectResponse(url="/", status_code=303)

    storage.add_entry(num1, op, num2, result)
    return RedirectResponse(url="/", status_code=303)


@app.post("/clear")
def clear_history():
    storage.clear_entries()
    return RedirectResponse(url="/", status_code=303)


@app.post("/delete/{entry_id}")
def delete_entry(entry_id: int):
    if hasattr(storage, "delete_entry"):
        storage.delete_entry(entry_id)
    else:
        entries = storage.all_entries()
        entries[:] = [e for e in entries if e.get("id") != entry_id]
    return RedirectResponse(url="/", status_code=303)