# ⚡ Fast API - Web Sockets

## Environment

```bash
pyenv local 3.10.0

python -m venv .venv \
  && source .venv/bin/activate \
  && python -m pip install --upgrade pip \
  && pip install -r requirements.txt
```

## Application

```bash
uvicorn main:app --reload
```
