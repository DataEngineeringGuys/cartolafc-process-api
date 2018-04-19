# -*- coding: utf-8 -*-
import os
from mapping import cartolafc_endpoint
from cartolafc_utils import cartolafc_dataframe, export_csv, get_api_cartolafc
from config import config_log

def mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    logger = config_log()

    logger.info("Criação de diretório temporário")
    tmp = 'extract\\data\\'
    mkdir(tmp)
    tmp = tmp + '{}.csv'

    rodada = get_api_cartolafc('https://api.cartolafc.globo.com/partidas')
    rodada = str(rodada['rodada']-1)

    logger.info("Inicio de extração de dados do Cartola FC")
    for k, v in cartolafc_endpoint.items():
        response = get_api_cartolafc(v[0])
        if response != None:
            df = cartolafc_dataframe(response, k)
            export_csv(df, tmp, k+'_'+rodada)
            logger.info("Arquivo %s exportado."%(k))

    logger.info("Extração concluida com sucesso.")
    

if __name__ == "__main__":
    main()