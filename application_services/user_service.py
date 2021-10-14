import uuid
from application_services.base_application_resource import BaseApplicationResource

db_name = "users"
table_name = "user"
address_table_name = "address"
user_address_table_name = "users_address"

def get_all_user():
    return BaseApplicationResource.get_by_template(db_name, table_name, None)

def get_user_by_id(user_id):
    template = {"uid": user_id}
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
    template = {"uid": userID}
    BaseApplicationResource.delete(db_name, table_name, template)

def get_address_by_uid(userID):
    template = {"uid": userID}
    addr_list = BaseApplicationResource.get_by_template(db_name, user_address_table_name, template)
    aids = []
    for addr in addr_list:
        aids.append(addr['aid'])
    addresses = BaseApplicationResource.find_in_condition(db_name, address_table_name, None, "aid", aids)
    return addresses


def create_address_by_uid(userID, create_data):
    # check if address exists?
    aid = insert_address(create_data)
    template = {"uid": userID, "aid": aid}
    BaseApplicationResource.create(db_name, user_address_table_name, template)