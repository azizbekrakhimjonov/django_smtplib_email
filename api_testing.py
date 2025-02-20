import requests

# post api testing
# api_url = ' http://127.0.0.1:8000/email/add/'
# data = {
#         "name": "Ali Axmedov",
#         "age": 31,
#         "department": "Electric",
#         "salary": "1000.00"
#         }
#
# response = requests.post(api_url, json=data)
# print(response.status_code)


api_url = 'http://127.0.0.1:8000/email/send/'
data = {
        'email': 'tomsmith@gmail.com',
        }

response = requests.post(api_url, json=data)
print(response.status_code)