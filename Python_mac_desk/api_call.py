import requests
response = requests.get("https://reqres.in/api/users/2")
print(response.text, response.status_code)

