# -*- coding: utf-8 -*-
from requests import post, get
import os
import sys
from mapping import cartolafc_endpoint
import pandas as pd
import json
from config import config_log

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
        return pd.DataFrame.from_dict(body)
    elif(TypeReturn in ['index']):
        return pd.DataFrame.from_dict(body, orient='index')
    else:
        df = pd.DataFrame.from_dict(body['atletas'], orient='index')
        df2 = df['scout'].apply(pd.Series)
        df3 = pd.merge(df, df2, left_index=True, right_index=True)
        df3['atleta_id'] = df.index
        del df3['scout'], df3['foto']
        return df3




def main():
    logger = config_log()

    logger.info("Autenticação no Cartola FC")
    # email = os.environ["USER_CARTOLA"]
    # password = os.environ["PASS_CARTOLA"]
    # token_auth = auth_cartolafc(email, password)

    logger.info("Autenticado com sucesso!")
    rm_endpoints = ['partida_rodada', 'busca_clube', 'busca_clube_slug', 'busca_clube_slug_rodada', 'busca_liga', 'busca_liga_slug']

    logger.info("Criação de diretório temporário")
    tmp = 'extract\\data\\'
    mkdir(tmp)
    tmp = tmp + '{}.csv'
    logger.info("Criado com sucesso!")

    logger.info("Inicio de extração de dados do Cartola FC")
    for k, v in cartolafc_endpoint.items():
        if k not in rm_endpoints:
            response = get_api(v[0])
            if response != None:
                response = json.loads(response)
                if k in response:
                    df = cartolafc_dataframe(response[k.replace('atletas_pontuados','atletas')],v[1])
                else:
                    df = cartolafc_dataframe(response, v[1])
                logger.info("Arquivo %s exportado."%(k))
                
                df.to_csv( (tmp).format(k), index = False )
    logger.info("Extração concluida com sucesso.")
    

if __name__ == "__main__":
    main()