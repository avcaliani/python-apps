import uuid
from flask import Flask, jsonify, g # pip3 install flask
from flask_httpauth import HTTPTokenAuth
from TokenService import Token

"""
Fonts: 
- https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
- https://github.com/miguelgrinberg/REST-auth/blob/master/api.py
- https://flask-httpauth.readthedocs.io/en/latest/

Request Header:
"Authorization" : "SCHEME YOUR_TOKEN_VALUE"
    -> Example:
    "Authorization" : "Token eyJhbGciOiJIUzI1NiIsImlhdCI6MTUzMDE0NjE0NywiZXh"
"""

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Token')
# You can change scheme, but it will affect your request token

@app.route('/')
def home():
    return "Wellcome to PYToken (with token)<br>By @avcaliani"

@app.route('/api/token')
def get_auth_token():
    new_uuid = uuid.uuid4()
    return jsonify({ 
        'uuid': str(new_uuid),
        'token': Token.generate_auth_token(str(new_uuid)).decode('ascii')
    })

@app.route('/api/token', methods=['POST'])
@auth.login_required
def check_auth_token():
    return jsonify({'uuid': g.current_user})
    
@auth.verify_token
def verify_token(token):
    g.current_user = Token.verify_auth_token(token)
    return  g.current_user != None

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)