import requests
from pprint import pprint

def get_mex(interval: str):

    response = requests.get(
        f"https://api.mexc.com/api/v3/klines?symbol=ZEPHUSDT&interval={interval}"
    )
    rezult = []

    rezult.append(response.json()[-1])
    rezult.append(response.json()[-2])

    
    return rezult
