import requests
import json

url = 'https://www.starbucks.com.cn/api/stores/nearby'

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

params = {
    'lat': 39.904989,
    'lon': 116.405285,
    'limit': 10,
    'locale': 'ZH',
    'features': '',
    'radius': 100000
}

data = requests.get(url=url, headers=header, params=params).text
with open('test/star.json', 'w', encoding='utf-8') as f:
    f.write(data)
# data = json.loads(data)
# with open('test/star.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False)