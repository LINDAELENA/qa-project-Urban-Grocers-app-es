import sender_stand_request
import data

def get_kit_body (kit_name, auth_token):  #Función para cambiar el cuerpo del contenido de la solicitud
    headers_copy = data.headers.copy()  #Crea copia de los headers para no modificar original
    current_kit_body = data.kit_name.copy()  #Copia el diccionario con el cuerpo de la solicitud desde data
    current_kit_body["name"] = kit_name  #Cambia el valor del parámetro name
    return current_kit_body, headers_copy  #Devuelve un nuevo diccionario con el nombre

def get_new_user_token():  #Función para recibir token del nuevo usuario
    response_new_user_token = sender_stand_request.post_new_user(data.user_body)  #Guarda el resultado para crear un nuevo usuario
    user_auth_token = response_new_user_token.json().get("authToken")  #Extrae authToken del nuevo usuario
    return user_auth_token  #Devuelve authToken del nuevo usuario

#Función de prueba positiva de creación de un kit, código 201
def positive_assert(kit_name, auth_token):
    kit_body, headers = get_kit_body(kit_name, auth_token)  #Obtiene cuerpo de la solicitud y encabezados actualizados
    kit_body_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)  #Guarda el resultado de la solicitud para crear un kit

    assert kit_body_response.status_code == 201  #Comprueba si el código de estado es 201
    assert kit_body_response.json()["name"] == kit_name  #Comprueba que el campo "name" coincida con el enviado

#Función de prueba negativa, código 400 "No se han transmitido parámetros"
def negative_assert_no_parameters(kit_name, auth_token):
    kit_body, headers = get_kit_body(kit_name, auth_token)  #Obtiene cuerpo de la solicitud y encabezados actualizados
    kit_body_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)  #Guarda el resultado de la solicitud para crear un kit

    assert kit_body_response.status_code == 400  #Comprueba si el código de estado es 400
    assert kit_body_response.json()["code"] == 400  #Comprueba que el atributo de "code" en la respuesta es 400
    assert kit_body_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"  #Comprueba la respuesta en el atributo "message"

#Función de prueba negativa, código 400, validación del nombre
def negative_assert_code_400(kit_name, auth_token):
    kit_body, headers = get_kit_body(kit_name, auth_token)  #Obtiene cuerpo de la solicitud y encabezados actualizados
    kit_body_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)  #Guarda el resultado de la solicitud para crear un kit

    assert kit_body_response.status_code == 400  #Comprueba si el código de estado es 400
    assert kit_body_response.json()["code"] == 400  #Comprueba que el atributo de "code" en la respuesta es 400
    assert kit_body_response.json()["message"] == "El nombre debe contener sólo letras latino, "\
                                                  "un espacio y un guión. " \
                                                  "De 2 a 15 caracteres"  #Comprueba la respuesta en el atributo "message"

#Prueba 1 positiva. El número permitido de caracteres (1)
def test_1_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("a", auth_token)

#Prueba 2 positiva. El número permitido de caracteres (511)
def test_2_create_kit_511_letter_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC", auth_token)

#Prueba 3 negativa. El número de caracteres es menor que la cantidad permitida (0)
def test_3_create_kit_0_letter_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_no_parameters("", auth_token)

#Prueba 4 negativa. El número de caracteres es mayor que la cantidad permitida (512)
def test_4_create_kit_512_letter_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD", auth_token)

#Prueba 5 positiva. Se permiten caracteres especiales
def test_5_create_kit_symbol_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("\"№%@\",",auth_token)

#Prueba 6 positiva. Se permiten espacios
def test_6_create_kit_spaces_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("A Aaa", auth_token)

#Prueba 7 positiva. Se permiten números
def test_7_create_kit_numbers_in_name_get_success_response():
    auth_token = get_new_user_token()
    positive_assert("123", auth_token)

#Prueba 8 negativa. El parámetro no se pasa en la solicitud
def test_8_create_kit_no_parameters_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_no_parameters({}, auth_token)

#Prueba 9 negativa. Se ha pasado un tipo de parámetro diferente (número)
def test_9_create_kit_different_parameters_in_name_get_error_response():
    auth_token = get_new_user_token()
    negative_assert_code_400( { "name": 123 }, auth_token)