import requests

url = 'https://www.baidu.com'
data = requests.get(url=url)
print(data.encoding)
data = data.text.encode('ISO-8859-1').decode('utf-8')
print(data)
with open('test/baidu.html', 'w', encoding='utf-8') as f:
    f.write(data)