# 🌶 Py Flask API
By Anthony Vilarim Caliani

[![#](https://img.shields.io/badge/licence-MIT-blue.svg)](#) [![#](https://img.shields.io/badge/python-3-yellow.svg)](#)

## Description
Very simple RESTful API using _Flask_.

## Quick Start

> 👉 Before run this script make sure that you are using a Python 3 virtual environment ;)

```sh
# Start App
python main.py
```

## API Usage
```sh
# Return a task list
curl http://localhost:5000/tasks

# Return a specific task
curl http://localhost:5000/tasks/1

# Create new Task
curl -d '{ "title": "New Task", "description": "Awesome \\o/" }' \
     -H 'Content-Type: application/json' \
     -X POST http://localhost:5000/tasks
```
