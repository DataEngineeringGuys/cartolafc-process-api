from requests import post, get
import os
from mapping_endpoint import cartolafc_endpoint
import pandas as pd
import json

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def auth_cartolafc(user, pwd):
    auth = {"payload":{"email":user, "password":pwd, "serviceId": 438}}
    response = post(cartolafc_endpoint['autenticacao'][0], json=auth)
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

def cartolafc_dataframe(body, TypeReturn):
    if TypeReturn in ['list','dict']:
        return pd.io.json.json_normalize(body)
    else:
        return pd.DataFrame.from_dict(body, orient='index')


def main():
    email = os.environ["USER_CARTOLA"]
    password = os.environ["PASS_CARTOLA"]
    token_auth = auth_cartolafc(email, password)
    rm_endpoints = ['partida_rodada', 'busca_clube', 'busca_clube_slug', 'busca_clube_slug_rodada', 'busca_liga', 'busca_liga_slug']
    tmp = 'cartolafc-extract\\temp\\'
    mkdir(tmp)
    tmp = tmp + '{}.csv'

    for k, v in cartolafc_endpoint.items():
        if k not in rm_endpoints:
            response = get_api(v[0])
            if response != None:
                response = json.loads(response)
                if k in response:
                    df = cartolafc_dataframe(response[k],v[1])
                else:
                    df = cartolafc_dataframe(response, v[1])
                print("Export %s file"%(k))
                
                df.to_csv( (tmp).format(k), index = False )
    print("Arquivos exportados com sucesso!")
    

if __name__ == "__main__":
    main()