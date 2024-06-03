import configuration
import requests
import data

def post_new_user(body): #Para crear un nuevo usuario
    return requests.post(configuration.URL_SERVICE +  configuration.CREATE_USER_PATH,
                         json=body, headers=data.headers)

response = post_new_user(data.user_body)
print (response.status_code)
print (response.json())