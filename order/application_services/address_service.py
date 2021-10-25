'''
Function to deal with address table by using SQL commands
'''

from application_services.base_application_resource import BaseApplicationResource
import json
import uuid

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
        print(data)
        template = data
        address = BaseApplicationResource.get_by_template(DB, ADDRESS_TABLE, template)
        if address:
            return address[0]["aid"]
        else:
            aid = uuid.uuid4().hex
            template = {'aid': aid}
            template.update(data)
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
        return BaseApplicationResource.get_by_template(DB, ADDRESS_TABLE, template)
    except:
        print("ops, the address not found")


def update_address(aid, data):
    '''
    Function to update an address
    '''
    try:
        template = {'aid': aid}
        update_data = {}
        for item in data:
            if data[item] != "":
                update_data[item] = data[item]
        return BaseApplicationResource.update(DB, ADDRESS_TABLE, update_data, template)
    except:
        print ("ops, update addres failed")


def delete_address(aid):
    '''
    Function to delete an address record in address table by its aid
    '''
    try:
        template = {'aid':aid}
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
        template = {'aid':aid}
        return BaseApplicationResource.delete(DB, USER_ADDRESS_TABLE, template)
    except:
        print("ops, cannot delete record in user_address table")







