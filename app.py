from flask import Flask, Response, request
from flask_cors import CORS
import json
from application_services.AddressResource.address_service import AddressResource

import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# from application_services.UsersResource.user_service import UserResource

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


# @app.route('/imdb/artists/<prefix>')
# def get_artists_by_prefix(prefix):
#     res = IMDBArtistResource.get_by_name_prefix(prefix)
#     rsp = Response(json.dumps(res), status=200, content_type="application/json")
#     return rsp


# @app.route('/users/create')
# def get_users():
#     res = UserResource.get_by_template(None)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp

@app.route('/addresses', methods=["GET", "POST"])
def addresses():
    if request.method == "GET":
        res = AddressResource.get_by_template(None)
        # add pagination
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")

    elif request.method == "POST":
        data = request.args
        print(data)
        res = AddressResource.create(data)

        headers = [{"Location", "/addresses/" + str(res)}]
        rsp = Response("CREATED", status=201, headers=headers, content_type="text/plain")
    else:
        rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    return rsp


@app.route('/addresses/id', methods=["GET", "POST", "PUT", "DELETE"])
def addresses_id():
    addr_id = request.path_parameter["parameter_1"]

    if request.method == "GET":
        res = AddressResource.get_by_template(None)
        # add pagination
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")

    # elif request.method == "POST":
        # print(data)
        # res = AddressResource.create(data)

        # headers = [{"Location", "/addresses/" + str(res)}]
        # rsp = Response("CREATED", status=201, headers=headers, content_type="text/plain")
    else:
        rsp = Response("NOT IMPLEMENTED", status=501, content_type="text/plain")

    return rsp

# @app.route('/<db_schema>/<table_name>/<column_name>/<prefix>')
# def get_by_prefix(db_schema, table_name, column_name, prefix):
#     res = d_service.get_by_prefix(db_schema, table_name, column_name, prefix)
#     rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
#     return rsp


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
