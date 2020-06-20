import requests
import logging

def ip_get():
    try:
        ip = requests.get('https://api.ipify.org').text
        
        return ip
    
    except Exception as ex:
        logging.error(ex)
        raise ex