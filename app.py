import flask
from flask import *
from application_services.user_service import *
from application_services.address_service import *
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def index_page():
    # return render_template("index.html")
    return "This is the homepage."

# newsId = shortuuid.uuid(url)


@app.route('/users', methods=['GET', 'POST'])
def users():
    if flask.request.method == 'POST':
        # User form['user'] for data insertion -> None
        uid = insert_user(request.form)
        if uid == "Exist":
            return "This email has been registered.", 422
        res = {
                "location": f"/users/{uid}"
                }
        return json.dumps(res), 201

    elif flask.request.method == 'GET':
        # get_all_user_info() -> JSON()
        return json.dumps(get_all_user()), 200


@app.route('/users/<userID>', methods=['GET', 'POST', 'DELETE'])
def users_id(userID):
    if flask.request.method == 'GET':
        # return render_template("users_id.html", userID=userID, jsonfile=json.dumps(get_user_by_id(userID)))
        # get_user_info(userID) - userID get from url -> JSON
        res = get_user_by_id(userID)
        print(res)
        if len(res) == 0:
            return "Cannot find resource.", 404
        return json.dumps(get_user_by_id(userID)), 200

    elif flask.request.method == 'POST':
        # print(request.form)
        # update_user_info(userID) - userID get from url - request.form['user'] input form
        update_user(userID, request.form)
        return f"User {userID}'s info has been updated", 200
        # extract items from data about user's info name, email, etc.

    elif flask.request.method == "DELETE":
        # delete_user_info(userID) - userID get from url
        delete_user(userID)
        # return f"User {userID} is already deleted.", 204
        return {"hello":"world"}, 204

@app.route('/users/<userID>/address', methods=['GET', 'POST'])
def users_id_address(userID):
    if flask.request.method == 'POST':
        try:
            create_address_by_uid(userID, request.form)
            return "Address added successfully for user!"
        except Exception as e1:
            return "Failed to add address for user!"
        # Insert a new address
        # associate aid with uid -> get from selecting or email
        # Insert new record to user_address

    elif flask.request.method == 'GET':
        return json.dumps(get_address_by_uid(userID))
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
        # print(get_all_address())
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
