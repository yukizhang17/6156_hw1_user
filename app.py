import flask
from flask import *
from oauthlib.oauth2 import TokenExpiredError

from application_services.user_service import *
from application_services.address_service import *
import json
from flask_cors import CORS
from flask_dance.contrib.google import make_google_blueprint, google
from middleware import security, notification
import os

app = Flask(__name__)
CORS(app)

client_id = "533947044188-ph3626aekho0mifa5s6l4k5i20dqpdnh.apps.googleusercontent.com"
client_secret = "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"
app.secret_key = "anything works"

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
blueprint = make_google_blueprint(
    client_id=client_id,
    client_secret=client_secret,
    reprompt_consent=True,
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

g_bp = app.blueprints.get("google")


@app.before_request
def before_request_func():
    print("Before request: checking authorization")
    try:
        if google.authorized and request.endpoint != 'login':
            authenticated = security.check_security(request, google, g_bp)
            if not authenticated:
                return redirect(url_for("google.login"))
    except TokenExpiredError as e:
        return redirect(url_for("google.login"))

@app.after_request
def after_request_func(rsp):
    notification.notify(request)
    return rsp


@app.route('/')
def index_page():
    # return render_template("index.html")
    return "This is the homepage."


@app.route('/users', methods=['GET', 'POST'])
def users():
    if flask.request.method == 'POST':
        # User form['user'] for data insertion -> None
        uid = insert_user(request.form)
        if uid == "Exist":
            return "This email has been registered.", 422
        res = {"location": f"/users/{uid}"}
        return json.dumps(res), 201

    elif flask.request.method == 'GET':
        # get_all_user_info() -> JSON()
        return json.dumps(get_all_user()), 200


@app.route('/users/<userID>', methods=['GET', 'POST', 'DELETE'])
def users_id(userID):
    if flask.request.method == 'GET':
        # return render_template("users_id.html", userID=userID, jsonfile=json.dumps(get_user_by_id(userID)))
        res = get_user_by_id(userID)
        print(res)
        if len(res) == 0:
            return "Cannot find resource.", 404
        return json.dumps(get_user_by_id(userID)), 200

    elif flask.request.method == 'POST':
        update_user(userID, request.form)
        return f"User {userID}'s info has been updated", 200

    elif flask.request.method == "DELETE":
        delete_user(userID)
        return f"The user {userID} has been deleted", 204


@app.route('/users/<userID>/address', methods=['GET', 'POST'])
def users_id_address(userID):
    if flask.request.method == 'POST':
        try:
            create_address_by_uid(userID, request.form)
            return f"Address added successfully for user {userID}!", 201
        except Exception as e1:
            return "Failed to add address for user!", 400
    elif flask.request.method == 'GET':
        return json.dumps(get_address_by_uid(userID)), 200
        # return render_template("users_id_address.html", userID=userID, jsonfile=json.dumps(get_address_by_uid(userID)))

        # join user with user_address and return
    # elif flask.request.method == 'PUT':
    # 1. get aid
    # 2. delete <uid, aid> in user_address
    # 3. create a new address with request.form['address']
    # 4. insert to address table
    # 5. insert <uid, new aid> to user_address table


@app.route('/address', methods=['GET', 'POST'])
def address():
    if flask.request.method == 'POST':
        insert_address(request.form)
        return "You are all set"
        # check duplicate
        # insert a new address

    elif flask.request.method == 'GET':
        return json.dumps(get_all_address())


@app.route('/address/<addressID>', methods=['GET', 'POST', 'DELETE'])
def address_id(addressID):
    if flask.request.method == 'GET':
        return json.dumps(get_address_by_aid(addressID))
        # return render_template("address_id.html", addressID=addressID, jsonfile=json.dumps(get_address_by_aid(addressID)))

    elif flask.request.method == 'POST':
        update_address(addressID, request.form)
        return "Address has been updated."

    elif flask.request.method == "DELETE":
        # delete_user_info(userID) - userID get from url
        delete_address(addressID)
        return "Address is already deleted."


'''
@app.route('/address/<addressID>/users', methods=['GET', 'POST'])
def address_id_users(addressID):
    if flask.request.method == 'POST':
        return insert_user_by_addressid(addressID)

    elif flask.request.method == 'GET':
        return render_template("address_id_users.html", jsonfile=json.dumps(get_user_by_addressid(addressID)))
'''

if __name__ == '__main__':
    app.run()
