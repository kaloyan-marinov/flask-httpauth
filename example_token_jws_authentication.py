"""Token authentication example

This example demonstrates how to protect Flask endpoints with token authentication,
using tokens.
"""
from flask import Flask
from flask_httpauth import HTTPTokenAuth
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired,
)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret'

token_serializer = Serializer(app.config['SECRET_KEY'], expires_in=120)

auth = HTTPTokenAuth(scheme='Bearer')


users = [
    {'id': 1, 'username': 'john'},
    {'id': 2, 'username': 'susan'},
]
for user in users:
    user_data = {'id': user['id']}
    token = token_serializer.dumps(user_data).decode('utf-8')
    print(f'*** token for {user}: {token}')


@auth.verify_token
def verify_token(token):
    try:
        user_data = token_serializer.loads(token)
    except SignatureExpired:
        return None  # valid token, but expired
    except BadSignature:
        return None  # invalid token

    user = [u for u in users if u['id'] == user_data['id']]
    if len(user) == 1:
        return user[0]
    else:
        return None


@app.route('/')
@auth.login_required
def index():
    username = auth.current_user()['username']
    return {'message': f'Hello, {username}!'}


if __name__ == '__main__':
    app.run()
