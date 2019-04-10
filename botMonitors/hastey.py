import requests
from bs4 import BeautifulSoup
import json
import requests, time, datetime, names, random, json
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"User-Agent":user}
url = "https://hastey.io/api/status"
with open("config.json", "r") as f:
	JsonData = json.load(f)
	webhook  = JsonData["webhook"]

embed2 = {
		"content": "Initializing Hastey Monitor",
		"embeds": [{
			"title": "Made by jdrez",
			"url": "https://hastey.io/#/",
			"color": 65280,
			"thumbnail": {
				"url": "https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjCuoTayYThAhUn11kKHXfUBGAQjRx6BAgBEAU&url=https%3A%2F%2Ftwitter.com%2Fhasteyio&psig=AOvVaw18q7MZGk2Jkb5mwtNpsY01&ust=1552754039258433"
			},
			"fields": [
				{
					"name": "Stauts",
					"value": "Initialized"

				}]
		}]
	}
initMonitor = True
r = requests.post(webhook, json = embed2,headers = headers)
print("[" + str(datetime.datetime.now()) + "] Initialized")
initMonitor = False
while True:
    r = requests.get(url, headers = headers)
    info  = r.text
    stock = json.loads(info)["status"]
    if stock == "false":
        pass
        time.sleep(1)
    else:
        print("[" + str(datetime.datetime.now()) + "] Restock") 
        embed = {
				"content": "@here hastey restock",
				"embeds": [{
					"title": "LINK TO CHECKOUT",
					"url": "https://hastey.io/#/",
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
