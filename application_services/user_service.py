from re import template
import uuid
from application_services.base_application_resource import BaseApplicationResource

db_name = "users"
table_name = "user"

def get_all_user():
    return BaseApplicationResource.get_by_template(db_name, table_name, None)

def get_user_by_id(user_id):
    template = {"id": user_id}
    return BaseApplicationResource.get_by_template(db_name, table_name, template)

def insert_user(create_data):
    # ﬁprint(create_data['email'])
    email = create_data["email"]
    res = BaseApplicationResource.get_by_template(db_name, table_name, {"email": email})
    if res is not None:
        uid = uuid.uuid4().hex
        template = {"uid": uid}
        for item in create_data:
            template[item] = create_data[item]
        BaseApplicationResource.create(db_name, table_name, template)


def update_user(userID, update_data):
    template = {}
    for item in update_data:
        template[item] = update_data[item]
    # print(template)
    user_id_template = {"uid": userID}
    BaseApplicationResource.update(db_name, table_name, template, user_id_template)

def delete_user(userID):
    