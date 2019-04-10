import requests
import  datetime
import  time
import json
from dhooks import Embed, Webhook
headers = {
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive'
}
url = "http://api.net-a-porter.com/NAP/US/en/150/0/summaries"
ids =[]
def SendHook(name,price,productUrl,image,proid,status):
    client = Webhook("https://discordapp.com/api/webhooks/565625299753107471/0pe8umQLMBUXs96J8y2u7SwhkKD2r4HLunl1LCWQ06e1K8wisS2BDoFm18I9RYsl-YfR")
    global embed1
    embed1 = Embed()
    #embed1.color = None
    embed1.set_title(
        title=name,
        url=productUrl
    )
    embed1.set_thumbnail(image)
    embed1.add_field(
        name="Status",
        value=str(status),
        inline=True
    )
    embed1.add_field(
        name="Product URL",
        value=productUrl,
        inline=False
    )
    embed1.add_field(
        name="PID",
        value=proid,
        inline=True
    )
    embed1.add_field(
        name = "Price",
        value= price
    )
    embed1.set_footer(
        text=f"jdrez • {str(datetime.datetime.now())}",
        icon_url="https://cdn.discordapp.com/attachments/553047247466790924/565625485799850141/favicon-192x192.png"
    )
    client.send(embeds=[embed1])
def initMonitor():
    products = requests.get(url, headers = headers).json()["summaries"]
    for product in products:
        id = product["id"]
        ids.append(id)
    ids.remove(1125760)
    while True:
        products = requests.get(url, headers = headers).json()["summaries"]
        for newProduct in products:
            if newProduct["id"] not in ids:
                newID = newProduct["id"]
                name = newProduct["name"]
                print(f"[{str(datetime.datetime.now())}]NEW PRODUCT FOUND [{name}]")
                price = '{} {}'.format(newProduct["price"]["amount"], newProduct["price"]["currency"])
                prodURL = 'https://www.net-a-porter.com/us/en/product/{}'.format(newID)
                prodImg = 'https://cache.net-a-porter.com/images/products/{}/{}_fr_m.jpg'.format(newID, newID)
                if(newProduct["badges"][1] ==''):
                    status = '{}'.format(newProduct["badges"][0])
                else:
                    status = '{} | {}'.format(newProduct["badges"][0], newProduct["badges"][1])
                ids.append(newID)
                SendHook(name,price,prodURL,prodImg,newID,status)
initMonitor()
