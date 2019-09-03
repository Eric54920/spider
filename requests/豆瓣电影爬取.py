import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}
params = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '100'
}

response = requests.get(url=url, headers=headers, params=params)
list_data = response.json()
with open('douban.json', 'w', encoding='utf-8') as f:
    json.dump(list_data, f, ensure_ascii=False)