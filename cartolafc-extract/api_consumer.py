from requests import post
from os import environ
from mapping_endpoint import cartolafc_endpoint

def auth_cartolafc(user, pwd):
    auth = {"payload":{"email":user, "password":pwd, "serviceId": 438, "captcha": ""}}
    response = post(cartolafc_endpoint['autenticacao'], json=auth)
    return response.json()

def main():
    email = environ["USER_CARTOLA"]
    password = environ["PASS_CARTOLA"]
    response = auth_cartolafc(email, password)
    print(response)

if __name__ == "__main__":
    main()