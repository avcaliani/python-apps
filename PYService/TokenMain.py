# https://blog.miguelgrinberg.com/post/restful-authentication-with-flask
# https://github.com/miguelgrinberg/REST-auth/blob/master/api.py
import uuid
from flask import Flask, jsonify, abort, make_response # pip3 install flask
from flask_httpauth import HTTPBasicAuth
from TokenService import Token

app = Flask(__name__)
auth = HTTPBasicAuth()

@app.route('/')
def home():
    return "Wellcome to PYService (with token)<br>By @avcaliani"

@app.route('/api/token')
def get_auth_token():
    new_uuid = uuid.uuid4()
    print("[ @avcaliani ] New UUID: %s" % str(new_uuid))
    return jsonify({ 'token': Token.generate_auth_token(str(new_uuid)).decode('ascii') })

@app.route('/api/token', methods=['POST'])
@auth.login_required
def check_auth_token():
    return jsonify({'data': 'Yeah!!'})
    
@auth.verify_password
def verify_password(token):
    return Token.verify_auth_token(token) != None

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)