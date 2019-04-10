import requests
from bs4 import BeautifulSoup
import json
import requests, time, datetime, names, random, json
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {
    "User-Agent":user,
    'accept-encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json; charset=utf-8'
    
}
url = "https://ghostaio.com/api/release/status?api_key=401c4630-2243-4911-b3f7-0c9165dfc6b6"
#they like  to update this so it won't work if ur seeingthis without the right one
with open("config.json", "r") as f:
	JsonData = json.load(f)
	webhook  = JsonData["webhook"]
while True:
    s = requests.get("https://ghostaio.com/", headers = headers)
    time.sleep(2)
    r = requests.get(url, headers = headers)
    info  = r.text
    stock = json.loads(info)["ghost_message"]
    releaseID = json.loads(info)["releaseID"]
    if stock == "Sold Out":
        pass
        time.sleep(1)
    else:
        print("[" + str(datetime.datetime.now()) + "] Restock") 
        embed = {
				"content": "@here ghost restock",
				"embeds": [{
					"title": "LINK TO CHECKOUT",
					"url": "https://ghostaio.com/",
					"color": 65280,
                    "thumbnail": {
						"url": "https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjCuoTayYThAhUn11kKHXfUBGAQjRx6BAgBEAU&url=https%3A%2F%2Ftwitter.com%2Fhasteyio&psig=AOvVaw18q7MZGk2Jkb5mwtNpsY01&ust=1552754039258433"
					},
					"fields": [
						{
							"name": "Stauts",
							"value": stock,
							"inline": True

						},
                        {
							"name": "ReleaseID",
							"value": releaseID

						}
                        ]
				}]
			}
        r = requests.post(webhook, json = embed,headers = headers)
        time.sleep(1)
