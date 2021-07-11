from flask_pymongo import PyMongo
from flask_login import LoginManager
import flask
from werkzeug.security import generate_password_hash
import uuid

app = flask.Flask(__name__)
app.secret_key = 'abc'

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/user_infos")
db = mongodb_client.db

@app.route("/login/<username>")
def get_user_info(username):
    user_info = db.accounts.find_one({"_id":username})

    return flask.jsonify(user_info)

@app.route("/login/create/<username>")
def flask_create_user(username):
    create_user(username, "000000")

    return flask.jsonify(message='success')

def create_user(user_name, password):
    user = {
        "name": user_name,
        "password": generate_password_hash(password),
        "id": user_name
    }
    db.accounts.insert_one(user)

if __name__ == '__main__':
    app.run(debug=True)