# 🔒 Py Secure API
By Anthony Vilarim Caliani

[![#](https://img.shields.io/badge/licence-MIT-blue.svg)](#) [![#](https://img.shields.io/badge/python-3-yellow.svg)](#)

Very simple RESTful API using _Flask_ and Token Authentication.

## Quick Start

> 👉 Before run this script make sure that you are using a Python 3 virtual environment ;)

```sh
# Start App
python main.py
```

## API Usage
```sh
# Return your token ;)
curl http://localhost:5000/api/token

# Return User UUID based on Auth Token
curl -H 'Authorization: Bearer $TOKEN' \
     http://localhost:5000/api/user
```

## Related Links

- [Blog: RESTful Authentication with Flask](https://blog.miguelgrinberg.com/post/restful-authentication-with-flask)
- [Github: Rest Auth](https://github.com/miguelgrinberg/REST-auth/blob/master/api.py)
- [Flask Docs: HTTP Auth](https://flask-httpauth.readthedocs.io/en/latest/)
