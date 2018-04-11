# -*- coding: utf-8 -*-
import pandas as pd
from extract.mapping import columns_dataset_casa, grandes_clubes, posicoes_map
from extract.config import config_log

logger = config_log()
# columns_atletas = ['apelido', 'atleta_id', 'clube_id', 'jogos_num', 'media_num', 'nome', 'pontos_num', 'posicao_id', 'preco_num', 'rodada_id', 'scout', 'status_id']
df_atletas = pd.read_csv(filepath_or_buffer='./extract/data/atletas.csv')
df_partidas = pd.read_csv(filepath_or_buffer='./extract/data/partidas.csv')
df_clubes = pd.read_csv(filepath_or_buffer='./extract/data/clubes.csv')
df_esquemas = pd.read_csv(filepath_or_buffer='./extract/data/esquemas_taticos.csv')

df_atletas_clube = pd.merge(df_atletas, df_clubes, how='inner', left_on=['clube_id'], right_on=['id'])

df_posicoes = pd.DataFrame.from_dict(posicoes_map, orient='index')
df_posicoes.rename(columns = {'nome': 'descricao_posicao', 'abreviacao': 'abreviacao_posicao'}, inplace = True)

df_atletas_clube_partidas = pd.merge(df_atletas_clube, df_partidas, how='inner', left_on=['id'], right_on=['clube_casa_id'])

# dataset casa
dataset = pd.merge(df_atletas_clube_partidas, df_posicoes, how='inner', left_on=['posicao_id'], right_on=['id'])
dataset = dataset[[i for i in columns_dataset_casa.keys()]]
dataset.rename(columns = columns_dataset_casa, inplace=True)

del df_atletas, df_atletas_clube, df_atletas_clube_partidas, df_clubes, df_esquemas, df_partidas, df_posicoes

# Selecionando jogadores do time casa
result_ = dataset[['apelido','abreviacao_clube', 'preco_num', 'descricao_posicao']].loc[ (dataset['nome_clube'].isin([i for i in grandes_clubes.keys()])) \
& (dataset['status_id'] == 7)  ]
result = result_.drop_duplicates()
result.to_csv('escalacao_opcoes.csv', index = False, encoding = 'utf-8-sig')


