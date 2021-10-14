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

