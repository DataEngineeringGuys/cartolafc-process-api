# -*- coding: utf-8 -*-
import pandas as pd

df_atletas = pd.read_csv(filepath_or_buffer='./cartolafc-extract/data/atletas.csv')
df_partidas = pd.read_csv(filepath_or_buffer='./cartolafc-extract/data/partidas.csv')
df_clubes = pd.read_csv(filepath_or_buffer='./cartolafc-extract/data/clubes.csv')

df_atletas_clube = pd.merge(df_atletas, df_clubes, how='inner', left_on=['clube_id'], right_on=['id'])

# dataset casa
dataset = pd.merge(df_atletas_clube, df_partidas, how='inner', left_on=['id'], right_on=['clube_casa_id'])
# dataset visitante
dataset_visitante = pd.merge(df_atletas_clube, df_partidas, how='inner', left_on=['id'], right_on=['clube_visitante_id'])

# Selecionando jogadores do time casa
print(dataset[['apelido','abreviacao']].loc[dataset['partida_id'] == 221169])
#
print(dataset_visitante[['apelido','abreviacao']].loc[dataset_visitante['partida_id'] == 221169])