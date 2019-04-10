import requests
from bs4 import BeautifulSoup
import json
import requests, time, datetime, names, random, json
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"User-Agent":user}
url1 = "https://api.adept-bots.com/api/stock?type=Lifetime"
url2 = "https://api.adept-bots.com/api/stock?type=Seasonal"
with open("config.json", "r") as f:
	JsonData = json.load(f)
	webhook  = JsonData["webhook"]
while True:
    r1 = requests.get(url1, headers = headers).json()["buttonText"]
    r2 = requests.get(url2, headers = headers).json()["buttonText"]
    if r1 != "Sold Out":
        print("[" + str(datetime.datetime.now()) + "] Restock") 
        embed = {
				"content": "@here adept  lifetime restock",
				"embeds": [{
					"title": "LINK TO CHECKOUT",
					"url": "http://adept-bots.com/",
					"color": 65280,
                    "thumbnail": {
						"url": "https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjCuoTayYThAhUn11kKHXfUBGAQjRx6BAgBEAU&url=https%3A%2F%2Ftwitter.com%2Fhasteyio&psig=AOvVaw18q7MZGk2Jkb5mwtNpsY01&ust=1552754039258433"
					},
					"fields": [
						{
							"name": "Stauts",
							"value": r1,
							"inline": True

						}]
				}]
			}
        r = requests.post(webhook, json = embed,headers = headers)
        time.sleep(1)
    if r2 != "Sold Out":
        print("[" + str(datetime.datetime.now()) + "] Restock") 
        embed = {
				"content": "@here adept  seasonal restock",
				"embeds": [{
					"title": "LINK TO CHECKOUT",
					"url": "http://adept-bots.com/",
					"color": 65280,
                    "thumbnail": {
						"url": "https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjCuoTayYThAhUn11kKHXfUBGAQjRx6BAgBEAU&url=https%3A%2F%2Ftwitter.com%2Fhasteyio&psig=AOvVaw18q7MZGk2Jkb5mwtNpsY01&ust=1552754039258433"
					},
					"fields": [
						{
							"name": "Stauts",
							"value": r2,
							"inline": True

						}]
				}]
			}
        r = requests.post(webhook, json = embed,headers = headers)
        time.sleep(1)
    else:
        pass
        time.sleep(1)
        