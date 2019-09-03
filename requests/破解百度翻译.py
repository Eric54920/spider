import requests
import json

post_url = 'https://fanyi.baidu.com/sug?'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}
word = input('enter a word:')
data = {
    'kw': word
}
response = requests.post(post_url, params=data, headers=headers)
res = response.json()['data']
for i in res:
    print(f"[{i['k']}]: {i['v']}")