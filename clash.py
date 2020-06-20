import requests
import json
import re
import csv
import pandas as pd
import logging
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='clash.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def ip_get():
    try:
        ip = requests.get('https://api.ipify.org').text
        logger.console(ip)
        # print(ip)
        
        return ip
    
    except Exception as ex:
        logging.error(ex)
        raise ex

def get_clan(token):
    try:  
        logger.console("ENTROU NO GET CLAN")
        logging.info("Acessando os clans com nome 'The resistance'")
        
        # setando parametros de requisição
        url_clans = "https://api.clashroyale.com/v1/clans/?tag=%239V2Y&name=The resistance"
        payload = {}
        headers = {
        'Authorization': 'Bearer {}'.format(str(token))
        }
        
        logging.warning("Utilizando o Token fixado no codigo")
        
        # Efetuando chamada a api passando o nome do clan como referencia
        response = requests.get(url_clans, headers=headers, data = payload)
        data = response.text.encode('utf8')
        
        # Corvertendo retorno para json
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
            
            # Retorna Tag tratada para segunda chamada              
            print(tag_corrigida)
            logger.console(tag_corrigida)

        logger.console("ENTROU NO GET MEMBERS")
        logging.info('Acessando os membros do clan usando a tag do clan')
        
        # Setando parametros para a chamada de membros do clan, passando a variavel da Tag formatada
        url_clans_members = "https://api.clashroyale.com/v1/clans/{}/members".format(str(tag_corrigida))
        payload = {}
        headers = {
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg2YWVjZDEyLWU0NTYtNGEwNS05NzNlLTgyZDcwODEyYTYwYiIsImlhdCI6MTU5MjQ1MDcyNCwic3ViIjoiZGV2ZWxvcGVyLzQ1ODU4MmVjLTNhNDgtZDUzNC1kNWZmLTdiYjBkMmI5ZTU2MiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzcuNDUuMzUuMjUiXSwidHlwZSI6ImNsaWVudCJ9XX0.e5FZ0AzCrW_VYVwI5D1PJCSAR6nJWU8YOdDMaL71TnJU6NkJ-JwILuSB7P5jximgxWv1nIaxi6IMgLU0weDu9w'
        }
        
        # Efetuando a segunda requisição a API
        response_clans_members = requests.get(url_clans_members, headers=headers, data = payload)
        
        # Convertendo retorno para texto
        data_clans_members = response_clans_members.text.encode('utf8')
        
        # Convertendo retorno para JSON
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
            
            # Retorna lista de informações dos membros do clan
            print(member_list)
            logger.console(member_list)
            
            return member_list
            
        logger.console("ENTROU NO SALVA CSV")
        logging.info('Gerando arquivo member_list.csv')
        
        # Convertendo a lista de informações de membros do clan em dataframe
        df = pd.DataFrame(member_list)
        
        # Salvando dataframe em formato CSV
        df.to_csv('member_list.csv', index=None, encoding='utf-8-sig')
        
        # Retorno 
        print("Sucesso!")
        logger.console("Sucesso!")
        
        return {}
        
    except Exception as ex:
        logging.error(ex)
        raise ex