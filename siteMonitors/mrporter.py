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
url = "http://api.net-a-porter.com/MRP/US/en/150/0/summaries"
ids =[]
def SendHook(name,price,productUrl,image,proid,status):
    client = Webhook("https://discordapp.com/api/webhooks/565627801072435232/-PqcddPV0FG3mGucvU__zpTSPlcdC12MQ9kq_3X0QJW5DwwFKT6htY9-qtq_QEtYwz0t")
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
        icon_url="https://cdn.discordapp.com/attachments/553047247466790924/565627921344102431/porter.jpg"
    )
    client.send(embeds=[embed1])
def initMonitor():
    products = requests.get(url, headers = headers).json()["summaries"]
    for product in products:
        id = product["id"]
        ids.append(id)
    ids.remove(1069217)
    while True:
        products = requests.get(url, headers = headers).json()["summaries"]
        for newProduct in products:
            if newProduct["id"] not in ids:
                newID = newProduct["id"]
                name = newProduct["name"]
                print(f"[{str(datetime.datetime.now())}]NEW PRODUCT FOUND [{name}]")
                price = '{} {}'.format(newProduct["price"]["amount"], newProduct["price"]["currency"])
                prodURL = 'https://www.net-a-porter.com/us/en/product/{}'.format(newID)
                prodImg = 'https://cache.mrporter.com/images/products/{}/{}_mrp_ou_m2.jpg'.format(newID, newID)
                #/cache.mrporter.com/images/products/1069217/1069217_mrp_{{shot}}_{{size}}.jpg"
                status = '{}'.format(newProduct["badges"][0])
                ids.append(newID)
                SendHook(name,price,prodURL,prodImg,newID,status)
initMonitor()
