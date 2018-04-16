# -*- coding: utf-8 -*-
import pandas as pd
from requests import post, get
import json

def get_api_cartolafc(url, **kwargs):
    response =  get(url, **kwargs)
    if response.status_code != 200:
        None
    else:
        return json.loads(response.content.decode())

def set_credentials_cartolafc(user, pwd):
    url = 'https://login.globo.com/api/authentication'
    auth = {"payload":{"email":user, "password":pwd, "serviceId": 438}}
    response = post(url, json=auth)
    if 'glbId' not in response.json():
        raise ValueError(response.json()['id'])
    else: 
        return response.json()['glbId']

def cartolafc_dataframe(body, file_name):
    if file_name in ['mercado_status', 'mercado_destaque', 'rodadas', 'esquemas_taticos']:
        return pd.io.json.json_normalize(body)
    elif file_name in ['patrocinadores', 'clubes']:
        df = pd.DataFrame.from_dict(body, orient='index')
        df['id_%s'%file_name] = df.index
        return df
    elif file_name in ['partidas', 'atletas']:
        df = pd.DataFrame.from_dict(body[file_name])
        return df
    elif file_name in ['atletas_pontuados']:
        df = pd.DataFrame.from_dict(body['atletas'], orient='index')
        df2 = df['scout'].apply(pd.Series)
        df3 = pd.merge(df, df2, left_index=True, right_index=True)
        df3['atleta_id'] = df.index
        del df3['scout'], df3['foto']
        return df3
    else:
        None


def export_csv(dataframe, dir, filename):
    dataframe.to_csv( (dir).format(filename), index = False )