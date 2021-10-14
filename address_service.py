'''
Function to deal with address table by using SQL commands
'''

from application_services.base_application_resource import BaseApplicationResource
import json

'''
Global field
'''
DB = "users"
ADDRESS_TABLE = "address"
USER_ADDRESS_TABLE = 'user_address'





def insert_address(data):
    '''
    Function to insert a new address entry to adress table
    '''
    try:
        template = json.loads(data)
        if base_application_resource.get_by_template(DB, ADDRESS_TABLE, template):
            return "Address already exists."
        else:
            aid = uuid.uuid4().hex
            template = {'aid': aid}
            template.update(json.loads(data))
            res = BaseApplicationResource.create(DB, ADDRESS_TABLE, template)
            print(res)
            return aid
    except:
        print("ops, address instert failed")


def get_all_address():
    '''
    Function to query all adress data entries form address table
    '''
    try:
        res = BaseApplicationResource.get_by_template(DB, ADDRESS_TABLE, None)
    except:
        print("Ops, query of all adresses failed")
    return res


def get_address_by_aid(aid):
    '''
    Function to query a sepcific address by its aid
    '''
    try:
        template = {"aid": aid}
        return BaseApplicationResource.get_by_template(db_name, table_name, template)
    except:
        print("ops, the address not found")


def update_address(aid, data):
    '''
    Function to update an address
    '''
    try:
        template = {'aid': aid}
        return BaseApplicationResource.update(DB, ADDRESS_TABLE, json.loads(data), template)
    except:
        print ("ops, update addres failed")


def delete_address(aid):
    '''
    Function to delete an address record in address table by its aid
    '''
    try:
        template = ['aid': aid]
        print(delete_address_user(aid))
        return BaseApplicationResource.delete(DB, ADDRESS_TABLE, template)
    except:
        print("ops, delete rocord in address table failed")


def delete_address_user(aid):
    '''
    Helper function to delete records in user_address table when action of
    delete user or address happens.
    '''
    try:
        template = ['aid': aid]
        return BaseApplicationResource.delete(DB, USER_ADDRESS_TABLE, template)
    except:
        print("ops, cannot delete record in user_address table")

'''
def get_user_by_addressid(aid):
    '''
   # Function to get all users at a specific address by aid
    '''
    try:
        template = {'aid': aid}

'''

'''
def insert_user_by_addressid(aid):
'''





