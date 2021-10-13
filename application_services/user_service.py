from re import template
from application_services.base_application_resource import BaseApplicationResource

db_name = "users"
table_name = "user"

def get_all_user():
    return BaseApplicationResource.get_by_template(db_name, table_name, None)

def get_user_by_id(user_id):
    template = {"id": user_id}
    return BaseApplicationResource.get_by_template(db_name, table_name, template)

# def insert_user(create_data):
    # BaseApplicationResource.create(db_name, table_name, create_data)
