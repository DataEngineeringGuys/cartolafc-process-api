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

df_final = pd.read_csv(filepath_or_buffer='./extract/data/Scouts.csv')
df_final = df_final.loc[df_final['Participou'] == True]
df_final = df_final.loc[df_final['atleta_id'] == 68808] # 38545 61033 36540
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


