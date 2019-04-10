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
url = "https://dashe.io/api/v1/status"
with open("config.json", "r") as f:
	JsonData = json.load(f)
	webhook  = JsonData["webhook"]
while True:
    r = requests.get(url, headers = headers)
    print(r.json)
    info  = r.text
    stock = json.loads(info)
    if stock == "false":
        pass
        time.sleep(1)
    else:
        print("[" + str(datetime.datetime.now()) + "] Restock") 
        embed = {
				"content": "@here dashe restock",
				"embeds": [{
					"title": "LINK TO CHECKOUT",
					"url": "https://dashe.io/",
					"color": 65280,
                    "thumbnail": {
						"url": "https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjCuoTayYThAhUn11kKHXfUBGAQjRx6BAgBEAU&url=https%3A%2F%2Ftwitter.com%2Fhasteyio&psig=AOvVaw18q7MZGk2Jkb5mwtNpsY01&ust=1552754039258433"
					},
					"fields": [
						{
							"name": "Stauts",
							"value": stock,
							"inline": True

						}]
				}]
			}
        r = requests.post(webhook, json = embed,headers = headers)
        time.sleep(1)
