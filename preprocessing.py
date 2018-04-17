# -*- coding: utf-8 -*-
import pandas as pd
from extract.mapping import columns_dataset_casa, grandes_clubes, posicoes_map, status_map
from extract.config import config_log
from functools import reduce
from sklearn import linear_model

logger = config_log()

## Atletas_pontuados 'A','CA','CV','DD','FC','FD','FF','FS','FT','G','GC','GS','I','PE','RB','SG'
# df_atletas_pontuados = pd.read_csv(filepath_or_buffer='./extract/data/atletas_pontuados.csv', usecols=['apelido','atleta_id','clube_id','jogos_num','media_num','nome',\
# 'pontos_num','posicao_id','preco_num','rodada_id','status_id','variacao_num'])
# df_atletas_pontuados.rename(columns={'nome':'nome_atleta', 'clube_id': 'id_clubes'}, inplace=True)
## Atletas
df_atletas = pd.read_csv(filepath_or_buffer='./extract/data/atletas_pontuados.csv', usecols=['apelido','atleta_id','clube_id','jogos_num','media_num','nome',\
'pontos_num','posicao_id','preco_num','rodada_id','status_id','variacao_num','A','CA','CV','DD','FC','FD','FF','FS','FT','G','GC','GS','I','PE','RB','SG'])
df_atletas.rename(columns={'nome':'nome_atleta', 'clube_id': 'id_clubes'}, inplace=True)
## Partidas
df_partidas = pd.read_csv(filepath_or_buffer='./extract/data/partidas.csv', usecols=['clube_casa_id', 'clube_visitante_id', 'aproveitamento_mandante', 'aproveitamento_visitante'])
df_partidas['id_clubes'] = df_partidas['clube_casa_id']
## Clubes
df_clubes = pd.read_csv(filepath_or_buffer='./extract/data/clubes.csv', usecols=['id_clubes', 'nome', 'abreviacao'])
df_clubes.rename(columns={'nome': 'nome_clube', 'abreviacao': 'abreviacao_clube'}, inplace=True)
## Status
df_status = pd.DataFrame.from_dict(status_map, orient='index')
df_status.rename(columns={'id': 'status_id', 'nome': 'nome_status'}, inplace=True)
## Posições
df_posicoes = pd.DataFrame.from_dict(posicoes_map, orient='index')
df_posicoes.rename(columns = {'nome': 'nome_posicao', 'abreviacao': 'abreviacao_posicao', 'id': 'posicao_id'}, inplace = True)

df_final = reduce(lambda left,right: pd.merge(left,right, on='id_clubes'), [df_atletas, df_clubes, df_partidas])
df_final = pd.merge(df_final, df_status, how='left', on='status_id')

df_final = pd.merge(df_final, df_posicoes, how='left', left_on='posicao_id', right_on='posicao_id')


# # Selecionando jogadores do time casa
# result_ = dataset.loc[ (dataset['nome_clube'].isin([i for i in grandes_clubes.keys()])) \
# & (dataset['status_id'] == 7)  ]

df_final.drop( df_final[df_final.nome_status == 'Nulo'].index, inplace=True )
# df_final.to_csv('escalacao_opcoes.csv', index = False, encoding = 'utf-8-sig', decimal=',')

dataset = df_final[['atleta_id', 'id_clubes', 'media_num', 'pontos_num', 'preco_num', 'status_id', 'variacao_num','A','CA','CV','DD','FC','FD','FF','FS','FT','G','GC','GS','I','PE','RB','SG', 'nome_status', 'posicao_id']]

dataset = dataset[dataset.nome_status == 'Provável']
dataset = dataset[dataset.posicao_id == 5]

X, y = dataset[['atleta_id', 'id_clubes', 'preco_num', 'variacao_num','A','CA','CV','DD','FC','FD','FF','FS','FT','G','GC','GS','I','PE','RB','SG']], dataset['pontos_num']
X = X.fillna(0)
lm = linear_model.LinearRegression()

result = lm.score(X,y)
logger.info("CSV exportado com sucesso!")


