from requests import get
from robot.libraries.BuiltIn import BuiltIn


class ipgetter():
    def ip_get(self):
        ip = get('https://api.ipify.org').text
        print(ip)
        return ip

ip = ipgetter()
varip = ip.ip_get()