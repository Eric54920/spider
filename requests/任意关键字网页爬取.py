import requests

url = 'https://www.baidu.com/s'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}
kw = input('enter a word:')
params = {
    'word': kw
}
response = requests.get(url=url, params=params, headers=headers)
res = response.text
filename = kw + '.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(res)