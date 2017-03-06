import cryptocompare_coin_list
from cryptocompare_coin_list import coinList
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
coinList = coinList.getCoinList()
def getCoinShapShot(coinlist):
    for index in range(len(coinlist)+1):
        if (index ==0):
            listOne = ['H1Text', "TotalCoinSupply", "Algorithm","proofType","startDate",
            "DifficultyAdjustment", "BlockRewardReduction", "BlockNumber", "BlockTime", "NetHashesPerSecond", "TotalCoinsMined",
            "BlockReward"]
        else:
            url = "https://www.cryptocompare.com/api/data/coinsnapshotfullbyid/?id=" + str(coinlist[index])
            r = requests.get(url, verify=False)
            data = r.json()
            print(coinlist[index])
            listOne = [data["Data"]["General"]['H1Text'], data["Data"]["General"]["TotalCoinSupply"], data["Data"]["General"]["Algorithm"], data["Data"]["General"]["ProofType"],data["Data"]["General"]["StartDate"],
            data["Data"]["General"]["DifficultyAdjustment"], data["Data"]["General"]["BlockRewardReduction"], data["Data"]["General"]["BlockNumber"], data["Data"]["General"]["BlockTime"], data["Data"]["General"]["NetHashesPerSecond"], data["Data"]["General"]["TotalCoinsMined"],
            data["Data"]["General"]["BlockReward"]]
        with open("cryptocompare_coin_shap_shot.csv", "a") as fp:
          wr = csv.writer(fp, dialect='excel')
          wr.writerow(listOne)
getCoinShapShot(coinList)
