# Team project

"A calculator that keeps a history"

## What this is

This app is a calculator that helps students to calculate different assignments. This calculator can add, subtract, multiply, and divide, and it saves the history of previous calculations.

## How to run it

You need Python 3.10 or newer.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000 in your browser. Stop it with `Ctrl+C`.

The entries are kept in memory: after a restart the list is empty again.

## Team

| GitHub         | Role   |
| KlentShutina15 | Seat 1 |
| Tbushi07       | Seat 2 |
| owen-debug3399 | Seat 3 |

## How we work

- Everyone clones the repository and creates their own branch with their real name.
- We write the issues we need to fix and work on as tasks.
- We separate the work equally and work on the issues together.
- After one pushes the code, the other two check it in pull requests and approve it.
- When we close an issue, we try to improve the app by adding extra features.

## Sources

2026-11-17: https://www.codechef.com/html-online-compiler -> we used it to see how the HTML and CSS code looked on a website.

## Use of AI

2026-11-16: Gemini, we used it for commands that weren't clear to us at the beginning.
2026-11-17: Gemini, we used it for code generation/debugging when we were stuck.
