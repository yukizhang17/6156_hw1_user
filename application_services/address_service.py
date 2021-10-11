from application_services.base_application_resource import BaseApplicationResource

db_name = "users"
table_name = "address"

def get_all_address():
    return BaseApplicationResource.get_by_template("users", "address", None)
