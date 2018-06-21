from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

class Token:
    
    APP_SECRET_KEY = "@avcaliani"
    
    @staticmethod
    def generate_auth_token(uuid, expiration = 600):
        serializer = Serializer(Token.APP_SECRET_KEY, expires_in = expiration)
        return serializer.dumps({ "uuid" : uuid })

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer(Token.APP_SECRET_KEY)
        try:
            data = serializer.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        return data['uuid']
