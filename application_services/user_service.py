from application_services.base_application_resource import BaseApplicationResource

db_name = "users"
table_name = "user"

def get_all_user():
    return BaseApplicationResource.get_by_template("users", "user", None)