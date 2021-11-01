import requests
import json

URL = "https://us-street.api.smartystreets.com/street-address"
AUTH_ID = "auth-id=f9eb6e09-ba17-5c76-b30b-9dc09132e188"
AUTH_TOKEN = "auth-token=kYia4umnZxd7pqmJ2sa5"


def varify_addr(addr):
    streets = addr['street_name1'].split(" ")
    streets.extend(addr['street_name2'].split(" "))

    street = "street=" + "+".join(streets)
    street = street[0:len(street) - 1]
    print(street)

    city = "city=" + addr['city']
    state = "state=" + addr['state']

    req = f"{URL}?{AUTH_ID}&{AUTH_TOKEN}&{street}&{city}&{state}&candidates=10"
    response = requests.get(req, "Content-Type: application/json")
    print(type(response))
    return response.json()


addr = {
        "street_name1": "70 Morningside Drive",
        "street_name2": "",
        "city": "New York",
        "state": "NY"
        }
print(varify_addr(addr))
