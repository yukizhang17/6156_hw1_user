from abc import ABC, abstractmethod
from database_services.base_rdb_service import BaseDataResource

class BaseApplicationException(Exception):

    def __init__(self):
        pass


class BaseApplicationResource(ABC):

    def __init__(self):
        pass

    @classmethod
    def get_by_template(cls, template):
        db_name, table_name = cls.get_data_resource_info()
        resource = BaseDataResource.find_by_template(db_name, table_name, template, None)
        result = cls.get_links(resource)
        return result


    @classmethod
    def get_by_resource_id(cls, key_values, field_list):
        pass

    @classmethod
    def create(cls, create_data):
        db_name, table_name = cls.get_data_resource_info()
        res = BaseDataResource.create(db_name, table_name, create_data)

        return res

    @classmethod
    def update(cls, update_data, template):
        db_name, table_name = cls.get_data_resource_info()
        res = BaseDataResource.update(db_name, table_name, update_data, template)
        return res

    @classmethod
    def delete(cls, record_id):
        db_name, table_name = cls.get_data_resource_info()
        res = BaseDataResource.delete(db_name, table_name, record_id)
        return res

    @classmethod
    @abstractmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    @abstractmethod
    def get_data_resource_info(cls):
        pass

#
# class BaseRDBApplicationResource(BaseApplicationResource):
#
#     def __init__(self):
#         super().__init__()
#
#     @classmethod
#     @abstractmethod
#     def get_by_template(cls, template):
#         pass
#
#     @classmethod
#     @abstractmethod
#     def get_links(cls, resource_data):
#         pass
#
#     @classmethod
#     @abstractmethod
#     def get_data_resource_info(cls):
#         pass
