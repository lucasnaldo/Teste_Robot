import requests
import json
import re
import os
import csv
import pandas as pd
import logging
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


def get_clan():
    try:
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        dir_path = os.getcwd()
        filename = 'clash_process.log'
        filenamepath = (dir_path + '\\' + filename)
        # logging.basicConfig(level=logging.DEBUG)
        logging.basicConfig(filename=filenamepath,
                            filemode='w',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
        token = BuiltIn().get_variable_value("${tokenstr}")
        logger.console(filenamepath)
        logger.console("Iniciando o processo de request da API")
        logging.info("Acessando os clans com nome 'The resistance'")
        
        # setando parametros de requisição
        url_clans = "https://api.clashroyale.com/v1/clans/?tag=%239V2Y&name=The resistance"
        payload = {}
        headers = {
        'Authorization': 'Bearer {}'.format(str(token))
        }
        
        logging.warning("url com parametro fixado no codigo")
        
        # Efetuando chamada a api passando o nome do clan como referencia
        response = requests.get(url_clans, headers=headers, data = payload)
        logger.console("\nConvertendo retorno em texto")
        data = response.text.encode('utf8')
        
        # Corvertendo retorno para json
        logger.console("Convertendo retorno em JSON")
        j_data = json.loads(data)
        items = j_data['items']
        
        # Criando nova lista
        listinha = []
        
        # Percorrendo a lista do retorno para pegar apenas as informações necessárias
        for item in items:
            dictzinho = {}
            if 'location' in item and item['location']:
                loc = item['location']
                if 'countryCode' in loc and loc['countryCode']:
                    
                    # Verificando clans que sejam do brasil
                    if loc['countryCode'] == 'BR':
                        
                        # Procurando começo da TAG
                        if re.search('#9V2Y', item['tag'], re.IGNORECASE):
                            dictzinho = item
                            tag = item['tag']
                            
                            # Salvando a Tag tratada em variavel
                            tag_corrigida = tag.replace('#', '%23')
                            listinha.append(dictzinho)

        logger.console("Tag do clan desejano encontrada e formatada")
        logging.info('Acessando os membros do clan usando a tag do clan')
        
        # Setando parametros para a chamada de membros do clan, passando a variavel da Tag formatada
        url_clans_members = "https://api.clashroyale.com/v1/clans/{}/members".format(str(tag_corrigida))
        payload = {}
        headers = {
        'Authorization': 'Bearer {}'.format(str(token))
        }
        logging.warning("Não utilize o Token fixado no codigo!")
        
        # Efetuando a segunda requisição a API
        logger.console("\nIniciando request dos membros do clan")
        response_clans_members = requests.get(url_clans_members, headers=headers, data = payload)
        
        # Convertendo retorno para texto
        logger.console("Convertendo retorno em texto")
        data_clans_members = response_clans_members.text.encode('utf8')
        
        # Convertendo retorno para JSON
        logger.console("Convertendo retorno em JSON")
        j_data_clans_members = json.loads(data_clans_members)
        items_clans_members = j_data_clans_members['items']
        
        # Criando nova lista
        member_list = []
        
        # Percorrendo a lista do retorno para pegar apenas as informações necessárias
        for item_member in items_clans_members:
            member = {}
            if 'name' in item_member and item_member['name']:
                member['nome'] = item_member['name']
            if 'expLevel' in item_member and item_member['expLevel']:
                member['level'] = item_member['expLevel']
            if 'trophies' in item_member and item_member['trophies']:
                member['troféus'] = item_member['trophies']
            if 'role' in item_member and item_member['role']:
                member['papel'] = item_member['role']
            
            member_list.append(member)            
            
        # Convertendo a lista de informações de membros do clan em dataframe
        logger.console("Transformando lista em dataframe")
        df = pd.DataFrame(member_list)
        
        # Salvando dataframe em formato CSV
        logging.info('Gerando arquivo member_list.csv')
        df.to_csv('member_list.csv', index=None, encoding='utf-8-sig')
        
        # Retorno 
        ret = "Processo finalizado com Sucesso!"
        logger.console(ret)
        
        return ret
        
    except Exception as ex:
        logging.error(ex)
        raise ex