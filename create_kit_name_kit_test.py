import sender_stand_request
import data

def get_kit_body (kit_name):  #Función para cambiar el cuerpo del contenido de la solicitud
    headers_copy = data.headers.copy()  #Crea copia de los headers para no modificar original
    current_kit_body = data.kit_name.copy()  #Copia el diccionario con el cuerpo de la solicitud desde data
    current_kit_body["name"] = kit_name  #Cambia el valor del parámetro name
    return current_kit_body, headers_copy  #Devuelve un nuevo diccionario con el nombre

def get_new_user_token():  #Función para recibir token del nuevo usuario
    response_new_user_token = sender_stand_request.post_new_user(data.user_body)  #Guarda el resultado para crear un nuevo usuario
    user_auth_token = response_new_user_token.json().get("authToken")  #Extrae authToken del nuevo usuario
    return user_auth_token  #Devuelve authToken del nuevo usuario