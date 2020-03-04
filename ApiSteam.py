import requests
import json

#  This is an API for Steam Spy. It accepts requests in GET string and returns data in JSON arrays.
#http://steamspy.com/api.php

def BuscaJogo(nome):
    req = requests.get('http://www.steamspy.com/api.php?request=all')
    dic = json.loads(req.text)
    results = []
    for appid in dic:
        jogo = dic[appid]
        if nome.upper() in jogo['name'].upper():
            results.append(jogo)
    return results

sair = False

while not sair:
    nome = input('Informe o nome do jogo ou digite SAIR: ')
    if nome.upper() != 'SAIR':
        jogos = BuscaJogo(nome)
        if jogos != []:
            for jogo in jogos:
                print(jogo['name'])
                print('Desenvolvedor:', jogo['developer'])
                print('Distribuidora:', jogo['publisher'])
                print('Aquisicoes:', jogo['owners'],'\n')
        else:
            print('Jogo nao localizado\n')
    else:
        sair = True