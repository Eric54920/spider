from bs4 import BeautifulSoup
import requests
import lxml

url = 'http://www.shicimingju.com/book/sanguoyanyi.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

response = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
li_list = soup.select('.book-mulu ul li')
fp = open('./sanguo.txt', 'w', encoding='utf-8')
for li in li_list:
	title = li.a.string
	detail_link = li.a['href']
	detail_url = 'http://shicimingju.com' + detail_link
	detail_data = requests.get(url=detail_url, headers=headers).text
	detail_soup = BeautifulSoup(detail_data, 'lxml')
	div_tag = detail_soup.find('div', class_='chapter_content')
	content = div_tag.text
	fp.write(title+':'+content+'\n')
	print(title+' ok')