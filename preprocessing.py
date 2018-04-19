# -*- coding: utf-8 -*-
import pandas as pd
from extract.mapping import grandes_clubes, posicoes_map, status_map, pontuacoes_map, columns_dataset_list
from extract.config import config_log
from functools import reduce
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import numpy as np
import matplotlib.pyplot as plt

logger = config_log()

## Atletas_pontuados 
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

df_final.drop( df_final[df_final.nome_status == 'Nulo'].index, inplace=True )
if 'DP' not in df_final.columns:
    df_final['DP'] = 0
if 'PP' not in df_final.columns:
    df_final['PP'] = 0

for i in pontuacoes_map.keys():
    df_final[i+'_value'] = df_final[i].apply(lambda x: x*pontuacoes_map[i])

df_final = df_final.fillna(0)

########## Create dataset
logger.info("Start processing")
from sklearn.ensemble import RandomForestRegressor

df_final = df_final[df_final.nome_status == 'Provável']
# 5 = Atacante
# df_final = df_final[df_final.posicao_id == 5]
df_final = df_final.fillna(0)
df_final = pd.read_csv(filepath_or_buffer='./extract/data/Scouts.csv')
df_final = df_final.loc[df_final['Participou'] == True]
# df_final = df_final.loc[df_final['atleta_id'] == 68808] # 38545 61033 36540

dataset = df_final[columns_dataset_list]
target = df_final['pontos_num'] 

X_train, X_test, y_train, y_test = train_test_split(dataset,target, train_size = 0.8)

lm = linear_model.LinearRegression()

lm.fit(X_train, y_train)
y_pred = lm.predict(X_test)
y_true = np.asarray(y_test)


df_df = pd.merge(pd.DataFrame(y_true), pd.DataFrame(y_pred), how='inner', left_index=True, right_index=True) 
residuals = y_test - y_pred

plt.scatter(y_test, y_pred, c="g", alpha=0.2)
plt.ylabel("Real Points")
plt.xlabel("Predict Points")
# plt.show()

# df_out = pd.merge(df_final, y_test[['preds']],how = 'left',left_index = True, right_index = True)

# print(df_out[['apelido', 'pontos_num','preds', 'preco_num']])

logger.info("Modelo gerado.")


