#!/usr/bin/python2.7
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import csv
url = "https://api.coinmarketcap.com/v1/ticker/"
r = requests.get(url, verify=False)
data = r.json()
for item in data:
    listOne = [item["symbol"], item["market_cap_usd"], item["total_supply"], item["last_updated"]]
    with open("coinmarketcap_summary.csv", "a") as fp:
      wr = csv.writer(fp, dialect='excel')
      wr.writerow(listOne)
