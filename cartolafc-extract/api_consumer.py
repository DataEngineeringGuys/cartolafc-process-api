from requests import post, get
from os import environ
from mapping_endpoint import cartolafc_endpoint
import pandas as pd
import json
from itertools import chain

def auth_cartolafc(user, pwd):
    auth = {"payload":{"email":user, "password":pwd, "serviceId": 438}}
    response = post(cartolafc_endpoint['autenticacao'], json=auth)
    if 'glbId' not in response.json():
        raise ValueError(response.json()['id'])
    else: 
        return response.json()['glbId']

def get_api(url, **kwargs):
    response =  get(url, **kwargs)
    if response.status_code != 200:
        None
    else:
        return response.content.decode()

def cartolafc_dataframe(body):
    if type(body) == list:
        return pd.io.json.json_normalize(body)
    elif type(body) == dict:
        return pd.DataFrame.from_dict(body, orient='index') 
    else:
        None

def main():
    # email = environ["USER_CARTOLA"]
    # password = environ["PASS_CARTOLA"]
    # response = auth_cartolafc(email, password)
    rm_endpoints = ['partida_rodada', 'busca_clube', 'busca_clube_slug', 'busca_clube_slug_rodada', 'busca_liga', 'busca_liga_slug']
    tmp = 'cartolafc-extract\\temp\\{}.csv'

    for k, v in cartolafc_endpoint.items():
        if k not in rm_endpoints:
            response = get_api(v)
            if response != None:
                response = json.loads(response)
                if k in response:
                    df = cartolafc_dataframe(response[k])
                else:
                    df = cartolafc_dataframe(response)
                print("Export %s file"%(k))
                
                df.to_csv( (tmp).format(k) )
    print("Arquivos exportados com sucesso!")
    

if __name__ == "__main__":
    main()