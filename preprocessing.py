# -*- coding: utf-8 -*-
import pandas as pd
from extract.mapping import grandes_clubes, posicoes_map, status_map, pontuacoes_map, columns_dataset_list
from extract.config import config_log
import numpy as np
import re

logger = config_log()

## Atletas_pontuados 
# df_atletas_pontuados = pd.read_csv(filepath_or_buffer='./extract/data/atletas_pontuados.csv', usecols=['apelido','atleta_id','clube_id','jogos_num','media_num','nome',\
# 'pontos_num','posicao_id','preco_num','rodada_id','status_id','variacao_num'])
# df_atletas_pontuados.rename(columns={'nome':'nome_atleta', 'clube_id': 'id_clubes'}, inplace=True)
## Atletas
df_atletas = pd.read_csv(filepath_or_buffer='./extract/data/atletas_pontuados.csv')
df_atletas.rename(columns={'nome':'nome_atleta', 'clube_id': 'id_clubes'}, inplace=True)
## Partidas
df_partidas = pd.read_csv(filepath_or_buffer='./extract/data/partidas.csv', usecols=['clube_casa_id', 'clube_visitante_id', 'placar_oficial_mandante', 'placar_oficial_visitante'])
df_partidas['id_clubes'] = df_partidas['clube_casa_id']
## Status
df_status = pd.DataFrame.from_dict(status_map, orient='index')
df_status.rename(columns={'id': 'status_id', 'nome': 'nome_status'}, inplace=True)
## Posições
df_posicoes = pd.DataFrame.from_dict(posicoes_map, orient='index')
df_posicoes.rename(columns = {'nome': 'nome_posicao', 'abreviacao': 'abreviacao_posicao', 'id': 'posicao_id'}, inplace = True)

df_final = pd.merge(df_atletas, df_partidas, how='left', left_on=['id_clubes'], right_on=['id_clubes'])

df_final = pd.merge(df_final, df_status, how='left', on='status_id')

df_final = pd.merge(df_final, df_posicoes, how='left', left_on='posicao_id', right_on='posicao_id')

df_final.drop( df_final[df_final.nome_status == 'Nulo'].index, inplace=True )
if 'DP' not in df_final.columns:
    df_final['DP'] = 0
if 'PP' not in df_final.columns:
    df_final['PP'] = 0

for i in pontuacoes_map.keys():
    df_final[i+'_value'] = df_final[i].apply(lambda x: x*pontuacoes_map[i])

df_final = df_final.fillna(0)


