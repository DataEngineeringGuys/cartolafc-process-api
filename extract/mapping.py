# -*- coding: utf-8 -*-
cartolafc_endpoint = {
"mercado_status": ["https://api.cartolafc.globo.com/mercado/status"],
"mercado_destaque": ["https://api.cartolafc.globo.com/mercado/destaques"],
"patrocinadores": ["https://api.cartolafc.globo.com/patrocinadores"],
"rodadas": ["https://api.cartolafc.globo.com/rodadas"],
"partidas": ["https://api.cartolafc.globo.com/partidas"],
"clubes": ["https://api.cartolafc.globo.com/clubes"],
"atletas": ["https://api.cartolafc.globo.com/atletas/mercado"],
"atletas_pontuados" : ["https://api.cartolafc.globo.com/atletas/pontuados"],
"esquemas_taticos": ["https://api.cartolafc.globo.com/esquemas"]
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