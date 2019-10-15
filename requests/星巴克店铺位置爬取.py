import requests
import json

url = 'https://www.starbucks.com.cn/api/stores/nearby?lat=39.904989&lon=116.405285&limit=1000&locale=ZH&features=&radius=100000'

headers = {
    'lat': '39.904989',
    'lon': '16.405285',
    'limit': '1000',
    'locale': 'ZH',
    'features':'',
    'radius': '100000'
}

response = requests.get(url=url, headers=headers)
json_data = json.loads(response.text)
with open('starbucks.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False)