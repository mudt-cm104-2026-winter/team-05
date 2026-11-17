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
    num1: str = Form(...),
    op: str = Form(...),
    num2: Optional[str] = Form(None),
):
    try:
        n1 = float(num1)
        n2 = float(num2) if num2 not in (None, "") else None
    except ValueError:
        return RedirectResponse(url="/", status_code=303)

    if op == "%":
        if n2 is not None:
            result = (n1 / 100) * n2
        else:
            result = n1 / 100
            n2 = 100
    else:
        if n2 is None:
            return RedirectResponse(url="/", status_code=303)

        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        elif op == "*":
            result = n1 * n2
        elif op == "/":
            result = n1 / n2 if n2 != 0 else "Error (division by zero)"
        else:
            return RedirectResponse(url="/", status_code=303)

    storage.add_entry(n1, op, n2, result)
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