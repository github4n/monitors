from proxymanager import ProxyManager
from datetime import datetime
import requests
import json
import time
import discord
import datetime
url = "https://api.nike.com//exp_snkrs/content/v1?country=us&language=en&offset=0&&orderBy=lastUpdated"
logo= "https://cdn.discordapp.com/attachments/505562520875040819/546905269540618240/breeze-bot-hex-pink.png"
webhook = "https://discordapp.com/api/webhooks/562731065907609632/Ga8FfcNYjEJGblE0bRvlBvv0fL3L5VNkMq96lBAz_r9H9gpFoCZXiUQgaoBkcrbComtq"

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"}
r = requests.get(url,  headers =headers)
threads = r.json()["threads"]
ids = []
for product in threads:
    ids.append(str(product["product"]["globalPid"]))
print(ids)
#ids.remove("2844216d-25f9-4158-9299-d54835d1682a")
while True:
    try:
        threads = requests.get(url, headers= headers).json()["threads"]
        for product in  threads:
            newID = product["product"]["globalPid"]
            if newID not in ids:
                print('[' + time.strftime("%I:%M:%S") + '] - NEW PRODUCT' + str(product["name"]))
                ids.append(newID)
                prodID  = product["id"]
                prodName = product["name"]
                description = product["seoDescription"]
                prodImage = product["product"]["imageUrl"]
                sizeArray = product["product"]["skus"]
                pid = product["product"]["globalPid"]
                url = "https://www.nike.com/launch/t/{}".format(product["seoSlug"])
                sizes = ''''''
                for size in sizeArray:
                    sizes += str(size["localizedSize"]) + "\n"
                embed = {
                        "embeds": [{
                                "title": prodName,
                                "description": description,
                                "url": url,
                                "color": 9583901,
                                "timestamp":str(datetime.datetime.now()),
                                "fields":[
                                    {
                                        "name": "Sizes",
                                        "value": sizes
                                    },
                                    {
                                        "name": "SNKRS ID",
                                        "value": prodID
                                    },
                                    {
                                        "name": "PID",
                                        "value": pid
                                    },
                                    
                                ],
                                "footer": {
                                    "icon_url": logo,
                                    "text": "snkrs monitor"
                                },

                                "image": {
                                    "url": prodImage
                                }
                            }]
                            }
                s = requests.post(webhook, data= json.dumps(embed), headers={'content-type':'application/json'})  
            else:
                pass
    except Exception as e:
        print(e)