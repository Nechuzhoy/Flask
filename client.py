import requests
from marshmallow import pprint

response = requests.get(
    'http://127.0.0.1:5000/api/',
)
print(response.status_code)
pprint(response.json())


# response = requests.post(
#     'http://127.0.0.1:5000/api/add_adv',
#     json={"title": "Три", "description":"Меняю", "owner":"Виктор"}
# )
# print(response.status_code)
# pprint(response.json())


# response = requests.get(
#     'http://127.0.0.1:5000/api/2',
# )
# print(response.status_code)
# pprint(response.json())


# response = requests.post(
#     'http://127.0.0.1:5000//api/delete/3',
# )
# print(response.status_code)
# pprint(response.json())


# response = requests.patch(
#     'http://127.0.0.1:5000/api/edit/4',
#     json={"title": "Tри", "description": "Меяю", "owner": "Bob"}
# )
# print(response.status_code)
# pprint(response.json())
