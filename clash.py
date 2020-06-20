import requests
import json
import re
import csv
import pandas as pd
import logging
from robot.libraries.BuiltIn import BuiltIn


logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='clash.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

try:  
    logging.info("Acessando os clans com nome 'The resistance'")
    url_clans = "https://api.clashroyale.com/v1/clans/?tag=%239V2Y&name=The resistance"
    payload = {}
    headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg2YWVjZDEyLWU0NTYtNGEwNS05NzNlLTgyZDcwODEyYTYwYiIsImlhdCI6MTU5MjQ1MDcyNCwic3ViIjoiZGV2ZWxvcGVyLzQ1ODU4MmVjLTNhNDgtZDUzNC1kNWZmLTdiYjBkMmI5ZTU2MiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzcuNDUuMzUuMjUiXSwidHlwZSI6ImNsaWVudCJ9XX0.e5FZ0AzCrW_VYVwI5D1PJCSAR6nJWU8YOdDMaL71TnJU6NkJ-JwILuSB7P5jximgxWv1nIaxi6IMgLU0weDu9w'
    }
    logging.warning("Utilizando o Token fixado no codigo")
    response = requests.get(url_clans, headers=headers, data = payload)
    data = response.text.encode('utf8')
    j_data = json.loads(data)
    items = j_data['items']
    listinha = []
    for item in items:
        dictzinho = {}
        if 'location' in item and item['location']:
            loc = item['location']
            if 'countryCode' in loc and loc['countryCode']:
                if loc['countryCode'] == 'BR':
                    if re.search('#9V2Y', item['tag'], re.IGNORECASE):
                        dictzinho = item
                        tag = item['tag']
                        tag_corrigida = tag.replace('#', '%23')
                        listinha.append(dictzinho)
                        
    
        
except Exception as ex:
    logging.error(ex)
    raise ex
        
try:
    logging.info('Acessando os membros do clan usando a tag do clan')
    url_clans_members = "https://api.clashroyale.com/v1/clans/{}/members".format(tag_corrigida)
    payload = {}
    headers = {
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6Ijg2YWVjZDEyLWU0NTYtNGEwNS05NzNlLTgyZDcwODEyYTYwYiIsImlhdCI6MTU5MjQ1MDcyNCwic3ViIjoiZGV2ZWxvcGVyLzQ1ODU4MmVjLTNhNDgtZDUzNC1kNWZmLTdiYjBkMmI5ZTU2MiIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxNzcuNDUuMzUuMjUiXSwidHlwZSI6ImNsaWVudCJ9XX0.e5FZ0AzCrW_VYVwI5D1PJCSAR6nJWU8YOdDMaL71TnJU6NkJ-JwILuSB7P5jximgxWv1nIaxi6IMgLU0weDu9w'
    }
    
    response_clans_members = requests.get(url_clans_members, headers=headers, data = payload)
    data_clans_members = response_clans_members.text.encode('utf8')
    j_data_clans_members = json.loads(data_clans_members)
    items_clans_members = j_data_clans_members['items']
    
    member_list = []
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
        
except Exception as ex:
    logging.error(ex)
    raise ex

try:
    logging.info('Gerando arquivo member_list.csv')
    df = pd.DataFrame(member_list)
    df.to_csv('member_list.csv', index=None, encoding='utf-8-sig')
    
except Exception as ex:
    logging.error(ex)
    raise ex