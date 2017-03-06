#https://www.cryptocompare.com/api/data/coinlist/
#!/usr/bin/python2.7
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
class coinList:
    @staticmethod
    def getCoinList():
        coinListId = []
        url = "https://www.cryptocompare.com/api/data/coinlist/"
        r = requests.get(url, verify=False)
        data = r.json()
    #    print(data["Data"]["BTC"])
        for item in data["Data"]:
            coinListId.append(int(data["Data"][item]["Id"]))
        return coinListId
