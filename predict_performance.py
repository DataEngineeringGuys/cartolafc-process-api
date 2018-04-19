import pandas as pd
from extract.mapping import grandes_clubes, posicoes_map, status_map, pontuacoes_map, columns_dataset_list
from extract.config import config_log
from functools import reduce
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import numpy as np
from sklearn.ensemble import RandomForestRegressor

logger = config_log()

logger.info("Start modeling")


# 5 = Atacante
# df_final = df_final[df_final.posicao_id == 5]

df_full = pd.read_csv(filepath_or_buffer='./extract/data/Scouts.csv')
df_final = df_full.loc[df_full['Participou'] == True]
df_final2 = df_final.loc[df_final['atleta_id'] == 61033] # 68808 61033 36540

df_partidas = pd.read_csv(filepath_or_buffer='./extract/data/partidas.csv', usecols=['clube_visitante_id', 'clube_visitante_posicao'])
df_partidas['Rodada'] = 38
df_final = pd.merge(df_final2, df_partidas, how='inner', left_on='id_clubes', right_on='clube_visitante_id')

print(df_final.head(50))


target = df_final['pontos_num'] 
dataset = df_final[columns_dataset_list]

X_train, X_test, y_train, y_test = train_test_split(dataset,target, train_size = 0.8)

rfr = RandomForestRegressor(100, min_weight_fraction_leaf=1).fit(X_train, y_train).predict(X_test)
print(rfr)
# rfr.fit(X_train, y_train)
# print(rfr.predict(X_test))



# lm = linear_model.LinearRegression()


# lm.fit(X_train, y_train)
# y_pred = lm.predict(X_test)
# y_true = np.asarray(y_test)


# df_df = pd.merge(pd.DataFrame(y_true), pd.DataFrame(y_pred), how='inner', left_index=True, right_index=True) 
# residuals = y_test - y_pred


# df_out = pd.merge(df_final, y_test[['preds']],how = 'left',left_index = True, right_index = True)

logger.info("Modelo gerado.")


