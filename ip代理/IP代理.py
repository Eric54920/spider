import requests

url = 'https://www.google.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

res = requests.get(url=url, headers=headers, proxies={'https':'202.182.118.147:443'}).text
with open('ip.html', 'w', encoding='utf-8') as f:
	f.write(res)