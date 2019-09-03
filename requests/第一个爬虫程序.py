import requests
import re

url = 'https://www.runoob.com'
response = requests.get(url = url)
res = response.text
print(res)
re1 = re.findall('http://.*|/*\.?[html]', res)
print(re1)
with open('bidainer.html', 'w', encoding='utf-8') as fp:
    fp.write(res)
print('ok')
