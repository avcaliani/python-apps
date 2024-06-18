# 🌎 Async HTTP

![License](https://img.shields.io/github/license/avcaliani/async-http?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.10.x-3776AB.svg?logo=python&logoColor=white)

## Quick Start

```bash
# 👇 Setting PyEnv version
pyenv local 3.10.1

# 👇 Virtual Environment
python -m venv .venv \
  && source .venv/bin/activate \
  && pip install --upgrade pip

# 👇 Dependencies
poetry install
```

When your environment is ready, you can execute this project.

### API

```bash
uvicorn api:app --reload
```

### Python Script

```bash
python main.py
```

#### Output
```bash
# Request 01
[0] status: 500 | run: 1
[1] status: 200 | run: 1
[4] status: 500 | run: 1
[2] status: 500 | run: 1
[5] status: 500 | run: 1
[3] status: 500 | run: 1

# Request 02
[0] status: 500 | run: 2
[4] status: 200 | run: 2
[2] status: 500 | run: 2
[3] status: 200 | run: 2
[5] status: 200 | run: 2

# Request 03
[0] status: 404 | run: 3
[2] status: 200 | run: 3

# Requests 04 to 10
[0] status: 404 | run: 4
[0] status: 404 | run: 5
[0] status: 404 | run: 6
[0] status: 500 | run: 7
[0] status: 500 | run: 8
[0] status: 500 | run: 9
[0] status: 500 | run: 10

# Data Results
[-1] {}
[200] {'id': '1', 'emoji': '🏈', 'queries': 1}
[200] {'id': '2', 'emoji': '🗿', 'queries': 1}
[200] {'id': '3', 'emoji': '🐍', 'queries': 1}
[200] {'id': '4', 'emoji': '💎', 'queries': 1}
[200] {'id': '5', 'emoji': '🍩️', 'queries': 1}

Elapsed time: 50.03
```

### References

- [FastAPI](https://fastapi.tiangolo.com/tutorial)
- [Blog: Asynchronous HTTP Requests in Python with aiohttp](https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp)

### The End
