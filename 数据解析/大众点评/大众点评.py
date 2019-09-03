from gevent import monkey;monkey.patch_all()
import gevent
from lxml import etree
from bs4 import BeautifulSoup
import requests
from multiprocessing import Process
from threading import Thread, Lock
import queue
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}


def task_p():
	task_t_list = []
	for i in range(2):
		t = Thread(target=task_t)
		t.start()

def task_t():
	task_c_list = []
	for i in range(5):
		href = q.get()
		g = gevent.spawn(task_c, href)
		task_c_list.append(g)
	gevent.joinall(task_c_list)

def task_c(url):
	res = requests.get(url=url, headers=headers).text
	soup = BeautifulSoup(res, 'lxml')
	total = soup.select('.content-wrap .page a:nth-last-child(2)')[0].string
	for i in range(1, int(total)):
		print(f'{i}/共{total}页')
		href = url + f'p{i}'
		sub_page = requests.get(url=href, headers=headers).text
		sub_soup = BeautifulSoup(sub_page, 'lxml')
		li_list = sub_soup.select('.content #shop-all-list li')
		for li in li_list:
			# 店铺名称
			title = li.select('.txt .tit a h4')[0].string
			# 评分
			rank = li.select('.txt .comment span')[0]['title']
			dic = {'title':title,'rank':rank}
			str = json.dumps(dic)
			fp.write(str+'\n')

if __name__ == '__main__':
	with open('links.txt','r', encoding='utf-8') as f:
		res = json.loads(f.read())
	q = queue.Queue(len(res))
	count = 0
	for i in res:
		if count < 16: # 从第16个链接开始爬取
			count += 1
			continue
		q.put(i)
	fp = open('data.json', 'a+', encoding='utf-8')
	task_lst = []
	for i in range(2):
		p = Process(target=task_p)
		task_lst.append(p)
	for i in task_lst:
		i.start()
	for i in task_lst:
		i.join()
	print('over')
