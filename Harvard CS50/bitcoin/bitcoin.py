import sys
import requests

def get_bitcoin_price():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice/BTC.json')
    data = response.json()
    price = data['bpi']['USD']['rate']
    price = price.replace(',', '')
    return float(price)
def multiplicacion():
    x=get_bitcoin_price()
    x2=x*float(sys.argv[1])
    valor= "${:,.4f}".format(x2)
    print(valor)

if __name__=="__main__":
    multiplicacion()