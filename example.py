from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth(app)


users = {
    'john': generate_password_hash('hello'),
    'susan': generate_password_hash('bye'),
}


@auth.verify_password
def verify_password(username, password):
    if (
        username in users
        and check_password_hash(users.get(username), password)
    ):
        return username
    return None


@app.route('/')
@auth.login_required
def index():
    return {'message': f'Hello, {auth.current_user()}!'}


if __name__ == '__main__':
    app.run()
