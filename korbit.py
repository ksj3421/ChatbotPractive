# -*- coding: utf-8 -*-

import requests
from datetime import datetime

def coin_detail(coin):
    base_url = 'https://api.korbit.co.kr/v1/ticker/detailed'
    url = '{}?currency_pair={}'.format(base_url, coin)
    response = requests.get(url)
    msg = message(response.json())
    return msg

def message(data):
    last_price = int(data.get('last'))
    high_price = int(data.get('high'))
    low_price = int(data.get('low'))
    bid_price = int(data.get('bid'))
    ask_price = int(data.get('ask'))
    timestamp = datetime.fromtimestamp(int(data.get('timestamp')/1000))

    return '''
KORBIT 현재가: {:,}
최근 24시간 최고가: {:,}
최근 24시간 최저가: {:,}
매수 호가: {:,}
매도 호가: {:,}
최종 체결 시각: {}
'''.format(last_price, high_price, low_price, bid_price, ask_price, timestamp)