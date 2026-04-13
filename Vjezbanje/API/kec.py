import requests

def get_cijena(coin, valuta="usd"):
    url = f"https://api.coinGecko.com/api/v3/simple/price?ids={coin}&vs_currencies={valuta}"

    response = requests.get(url)
    data = response.json()

    if coin in data:
        return data[coin][valuta]
    else:
        return None

def prikazi_portofolio(lista):
    print("=== Moj Portofolio ===")
    for coin in lista:
        cijena = get_cijena(coin)
        print(f"{coin}: {cijena} EUR")


portofolio = ["bitcoin", "ethereum", "solana"]
prikazi_portofolio(portofolio)


    
"""cijena = get_cijena("bitcoin")
print(f"Bitcoin: ${cijena}")

cijena2 = get_cijena("ethereum", "eur")
print(f"Ethereum: {cijena2} EUR")"""