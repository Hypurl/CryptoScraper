import requests as req
from lxml import html
def crypto(curr):
    print("searching {}........".format(curr))
    con=req.get("https://www.coindesk.com/price/"+curr)
    con=html.fromstring(con.content)
    price =con.xpath('/html/body/div/div[2]/main/section/div/div[1]/div/section/div/div/div[1]/div/section/div[1]/div[1]/div[2]/div/text()')
    change=con.xpath("/html/body/div[1]/div[2]/main/section/div/div[1]/div/section/div/div/div[1]/div/section/div[1]/div[2]/div[2]/div/span/span[1]")
    mc=con.xpath("/html/body/div/div[2]/main/section/div/div[1]/div/section/div/div/div[1]/div/section/div[1]/div[3]/div[2]/div")
    volume=con.xpath("/html/body/div/div[2]/main/section/div/div[1]/div/section/div/div/div[1]/div/section/div[1]/div[4]/div[2]/div")
    try:
        print("Price: {} | 24 Hour Change: {}%".format(str(price[0]), str(change[0].text)))
        print("Market Cap: {} | Volume(24H): {}".format(str(mc[0].text), str(volume[0].text)))
    except:
        print("Crypto not found.")

def save(items):
    for i in items:
        crypto(i)
    
inn=input("Search one or mutiple? ")
if inn == "1" or inn == "one":
    crypto(input("What do you want? "))
elif inn == "muti" or inn == "mutiple":
    allitems=input("what u want? ").split()
    save(allitems)
else:
    raise SystemExit

