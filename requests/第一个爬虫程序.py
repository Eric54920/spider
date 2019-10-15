import requests

url = 'https://www.runoob.com'
response = requests.get(url = url).text
with open('./bidainer.html', 'w', encoding='utf-8') as fp:
    fp.write(response)
print('ok')