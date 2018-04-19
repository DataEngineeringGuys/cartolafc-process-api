# -*- coding: utf-8 -*-
cartolafc_endpoint = {
"mercado_status": ["https://api.cartolafc.globo.com/mercado/status"],
"mercado_destaque": ["https://api.cartolafc.globo.com/mercado/destaques"],
# "patrocinadores": ["https://api.cartolafc.globo.com/patrocinadores"],
"rodadas": ["https://api.cartolafc.globo.com/rodadas"],
"partidas": ["https://api.cartolafc.globo.com/partidas"],
# "clubes": ["https://api.cartolafc.globo.com/clubes"],
"atletas": ["https://api.cartolafc.globo.com/atletas/mercado"],
"atletas_pontuados" : ["https://api.cartolafc.globo.com/atletas/pontuados"],
# "esquemas_taticos": ["https://api.cartolafc.globo.com/esquemas"]
}

cartolafc_endpoint_busca = {
"partida_rodada": ["https://api.cartolafc.globo.com/partidas/?q=rodada={rodada}"],
"busca_clube": ["https://api.cartolafc.globo.com/times?q={nome_time}"],
"busca_clube_slug": ["https://api.cartolafc.globo.com/time/slug/{slug_time}"],
"busca_clube_slug_rodada": ["https://api.cartolafc.globo.com/time/slug/{slug_time}/{rodada}"],
"busca_liga": ["https://api.cartolafc.globo.com/ligas?q={nome_liga}"],
"busca_liga_slug": ["https://api.cartolafc.globo.com/auth/liga/{slug_liga}"]
}

cartolafc_endpoint_user = {
"clubes_destaque": ["https://api.cartolafc.globo.com/pos-rodada/destaques"],
"info_clube_user": ["https://api.cartolafc.globo.com/auth/time"],
"info_clube_user_detalhes": ["https://api.cartolafc.globo.com/auth/time/info"],
"user_ligas": ["https://api.cartolafc.globo.com/auth/ligas"]
}


grandes_clubes = {"Flamengo":262,
"Botafogo":263,
"Corinthians":264,
"Fluminense":266,
"Vasco":267,
"Palmeiras":275,
"São Paulo":276,
"Santos":277,
"Cruzeiro":283,
"Grêmio":284,
"Internacional":285,
"Atlético-MG": 282}

posicoes_map = {"1":{"id":1,"nome":"Goleiro","abreviacao":"gol"},"2":{"id":2,"nome":"Lateral","abreviacao":"lat"},"3":{"id":3,"nome":"Zagueiro","abreviacao":"zag"},"4":{"id":4,"nome":"Meia","abreviacao":"mei"},"5":{"id":5,"nome":"Atacante","abreviacao":"ata"},"6":{"id":6,"nome":"Técnico","abreviacao":"tec"}}

status_map = {'2': {'id': 2, 'nome': 'Dúvida'}, '3': {'id': 3, 'nome': 'Suspenso'}, '5': {'id': 5, 'nome': 'Contundido'}, '6': {'id': 6, 'nome': 'Nulo'}, '7': {'id': 7, 'nome': 'Provável'}}

old_pontuacoes_map = [{"descricao": "Assistência",
"A": 5.0},
{"descricao": "Gol",
"G": 8.0},
{"descricao": "Finalização na trave",
"FT": 3.0},
{"descricao": "Falta sofrida",
"FS": 0.5},
{"descricao": "Finalização defendida",
"FD": 1.2},
{"descricao": "Finalização para fora",
"FF": 0.8},
{"descricao": "Cartão amarelo",
"CA": -2.0},
{"descricao": "Cartão vermelho",
"CV": -5.0},
{"descricao": "Defesa difícil",
"DD": 3.0},
{"descricao": "Falta cometida",
"FC": -0.5},
{"descricao": "Penalti perdido",
"PP": -4.0},
{"descricao": "Impedimento",
"I": -0.5},
{"descricao": "Gol contra",
"GC": -5.0},
{"descricao": "Gol sofrido",
"GS": -2.0},
{"descricao": "Passe errado",
"PE": -0.3},
{"descricao": "Roubada de bola",
"RB": -0.3},
{"descricao": "Jogo sem sofrer gols",
"SG": 5.0},
{"descricao": "Defesa de pênalti",
"DP": 7.0} ]

pontuacoes_map = {"A": 5.0, "G": 8.0, "FT": 3.0, "FS": 0.5, "FD": 1.2,
"FF": 0.8,
"CA": -2.0,
"CV": -5.0,
"DD": 3.0,
"FC": -0.5,
"PP": -4.0,
"I": -0.5,
"GC": -5.0,
"GS": -2.0,
"PE": -0.3,
"RB": -0.3,
"SG": 5.0,
"DP": 7.0} 


columns_dataset_list = ['atleta_id', 'id_clubes', 'Rodada_id','media_num', 'preco_num', 'status_id', 'variacao_num',
'A_value','CA_value','CV_value','DD_value','FC_value','FD_value','FF_value','FS_value',
'FT_value','G_value','GC_value','GS_value','I_value','PE_value','RB_value','SG_value', 'posicao_id']

# columns_dataset_list = ["Rodada","id_clubes","atleta_id","Participou","media_num","preco_num","variacao_num","FS","PE","A","FT","FD","FF","G","I","PP","RB","FC","GC","CA","CV","SG","DD","DP","GS"]