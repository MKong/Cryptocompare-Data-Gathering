import cryptocompare_coin_list
from cryptocompare_coin_list import coinList
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import datetime
import csv
coinList = coinList.getCoinList()
def getCoinSocialStats(coinlist):
    for index in range(len(coinlist)+1):
        if (index ==0):
            listOne = ['Name', "CoinName", "TwitterFollowers",
            "TwitterList", "TwitterFavourites", "TwitterAccount_Creation", "TwitterLink", "FacebookLikes", "FacebookLink",
            "RedditSubscribers","RedditActiveUsers", "RedditCommentsPerDay","RedditPostsPerDay", "RedditLink", "RepoStars", "RepoLanguage",
            "RepoForks", "url", "last_update", "RepoSubscribers"]
        else:
            url = "https://www.cryptocompare.com/api/data/socialstats/?id=" + str(coinlist[index])
            r = requests.get(url, verify=False)
            data = r.json()
            print(coinlist[index])
            #Check to see if Twitter, Facebook and Code Repository Exists
            if(data["Data"]["Twitter"]["Points"] ==0):
                 data["Data"]["Twitter"]["followers"] = "n/a"
                 data["Data"]["Twitter"]["lists"] = "n/a"
                 data["Data"]["Twitter"]["favourites"] = "n/a"
                 data["Data"]["Twitter"]["account_creation"] = "n/a"
                 data["Data"]["Twitter"]["link"] = "n/a"
            if(data["Data"]["Facebook"]["Points"] ==0):
                data["Data"]["Facebook"]["likes"] = "n/a"
                data["Data"]["Facebook"]["link"] = "n/a"
            if(data["Data"]["Reddit"]["Points"] ==0):
                data["Data"]["Reddit"]["subscribers"] = "n/a"
                data["Data"]["Reddit"]["active_users"] = "n/a"
                data["Data"]["Reddit"]["comments_per_day"] = "n/a"
                data["Data"]["Reddit"]["posts_per_day"] = "n/a"
                data["Data"]["Reddit"]["link"] = "n/a"
            if(data["Data"]["CodeRepository"]["Points"] ==0):
                data["Data"]["CodeRepository"]["List"] = [{"stars": "n/a", "language": "n/a", "forks": "n/a", "url": "n/a", "last_update": "n/a", "subscribers": "n/a"}]
            comments_per_day_exists = False
            for item in data["Data"]["Reddit"]:
                if(item =="comments_per_day"):
                    comments_per_day_exists = True
            if (comments_per_day_exists == False):
                data["Data"]["Reddit"]["comments_per_day"] = "n/a"

            listOne = [data["Data"]["General"]['Name'], data["Data"]["General"]["CoinName"], data["Data"]["Twitter"]["followers"], data["Data"]["Twitter"]["lists"],data["Data"]["Twitter"]["favourites"],
            data["Data"]["Twitter"]["account_creation"], data["Data"]["Twitter"]["link"], data["Data"]["Facebook"]["likes"],
            data["Data"]["Facebook"]["link"], data["Data"]["Reddit"]["subscribers"], data["Data"]["Reddit"]["active_users"],
            data["Data"]["Reddit"]["comments_per_day"],data["Data"]["Reddit"]["posts_per_day"],data["Data"]["Reddit"]["link"],
            data["Data"]["CodeRepository"]["List"][0]["stars"],data["Data"]["CodeRepository"]["List"][0]["language"],data["Data"]["CodeRepository"]["List"][0]["forks"],
            data["Data"]["CodeRepository"]["List"][0]["url"],data["Data"]["CodeRepository"]["List"][0]["last_update"],data["Data"]["CodeRepository"]["List"][0]["subscribers"]]
        with open("cryptocompare_socialstats.csv", "a") as fp:
          wr = csv.writer(fp, dialect='excel')
          wr.writerow(listOne)
getCoinSocialStats(coinList)
