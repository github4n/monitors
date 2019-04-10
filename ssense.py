import requests
import time
import json
from colorama import Fore, init 
import  datetime
import discord
from bs4 import BeautifulSoup
import datetime
init(autoreset=True)
user = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"User-Agent":user}
mainURL = "https://www.ssense.com/en-us/men.json"
logo= "https://cdn.discordapp.com/attachments/553047247466790924/565636044922290255/ssense.jpg"
webhook = "https://discordapp.com/api/webhooks/565636084806057986/i1FwOWeaa7-ZIAj7J2KWeHQwhY86ca0AQguuabPe0mO85c0jzosUsVnm9f760IdUl83O"

products = None
while True:
    responseget = requests.get(mainURL,headers = headers)
    response = json.loads(responseget.text)['products']
    if not products: products = response #saves products the first time
    if response != products: #if products does not equal the products on the page then do this
        index = -1
        for item in response: #gets the keys in the 'products' dict
            index += 1
            if item in products: continue #if key does not exist in your saved products then theres a new product on the page
            print('found new product')
            print(response[index]) #this will print the dict of the new product
            products = response #saves the new products
            for x in products:
                name = x["name"]
                print(f"[{str(datetime.datetime.now())}]NEW PRODUCT FOUND [{name}]")
                url = "https://ssense.com{}".format(x["url"])
                image = x["image"].replace('__IMAGE_PARAMS__', 'b_white/c_scale,h_820/f_auto,dpr_2.0')
                price = x["price"]["regular"]
                sku = x["sku"]
                color = 65280
                
                description = '''
                SKU: {}
                Price: {}
                '''.format(sku, price)
                
                
                embed = {
                "embeds": [{
                        "title": name,
                        "description": description,
                        "url": url,
                        "color": 9583901,
                        "timestamp": "2019-02-18T04:48:33.962Z",
                        "footer": {
                            "icon_url": logo,
                            "text": "ssense monitor"
                        },

                        "image": {
                            "url": image
                        }
                    }]
                    }
                s = requests.post(webhook, data= json.dumps(embed), headers={'content-type':'application/json'})  
                print(Fore.RED + name)
                print(Fore.CYAN + str(price))
                print(sku + "|" + url)
                print(image)
                print("-*"*20)
        