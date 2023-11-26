from flask import Flask
from flask_cors import CORS, cross_origin
from access_caspio import get_active_users


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://c2hbt072.caspio.com/"}})


@app.route("/users/active", methods=["GET"])
@cross_origin()
def get_active_users_endpoint():
    return get_active_users()


if __name__ == "__main__":
    app.run()
