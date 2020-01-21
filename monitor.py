import requests as rq
import bs4 
import time 
inp = input("Select The cryptocurrency that you want to monitor?\n1) BTC\n2) ETH\n3) XRP\n4) LTC\n")
if inp == '1':
    url = "https://cointelegraph.com/bitcoin-price-index"
    cryptocurrency = "Bitcoin"
elif inp == '2':
    url = "https://cointelegraph.com/ethereum-price-index"
    cryptocurrency = "Etherium"
elif inp == '3':
    url = "https://cointelegraph.com/xrp-price-index"
    cryptocurrency = "Ripple"
elif inp == '4':
    url = "https://cointelegraph.com/ltc-price-index"
    cryptocurrency = "Litecoin"
    
update_time = int(input("Update " + cryptocurrency + "\'s price in every ? seconds: "))
total_time = int(input("Monitor " + cryptocurrency + "\'s price for ? seconds: "))
headerss = {'User-Agent': 'Guptaji\'s_request'}

iterations = int( total_time/ update_time)
i = 0
while i <= iterations:
    r = rq.get(url, headers = headerss)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    with open("BTC_price_record.txt", "a+") as f:
        f.write(soup.find_all('div', attrs = {'class' : 'price-value'})[0].get_text() + "\n")
    time.sleep(update_time)