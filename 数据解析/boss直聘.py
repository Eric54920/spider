from bs4 import BeautifulSoup
import lxml
import requests

url = 'https://www.zhipin.com/job_detail/?query=python&city=101010100&industry=&position='

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

response = requests.get(url=url, headers=headers, proxies={'http':'58.217.94.5:8060'}).text

response = response.encode('ISO-8859-1').decode('utf-8')
print(response)

# soup = BeautifulSoup(response, 'lxml')

# li_list = soup.select('#main div div.job-list ul li')

# print(li_list)

