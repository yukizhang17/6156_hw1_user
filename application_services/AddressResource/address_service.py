from application_services.base_application_resource import BaseApplicationResource


class AddressResource(BaseApplicationResource):
    db_name = "users"
    table_name = "address"

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        for resource in resource_data:
            address_id = resource.get('id')

            links = []
            address_link = {"rel": "self", "href": "/addresses/" + str(address_id)}
            links.append(address_link)

            users_link = {"rel": "users", "href": "/users?address_id=" + str(address_id)}
            links.append(users_link)

            resource['links'] = links
            return resource_data


    @classmethod
    def get_data_resource_info(cls):
        return {cls.db_name, cls.table_name}
