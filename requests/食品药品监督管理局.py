import requests
import json
from threading import Thread

def getData(url, headers, data):
	response = requests.post(url=url, headers=headers, data=data).json()
	for dic in response['list']:
		ids_list.append(dic['ID'])

url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

ids_list = []

task = []

for i in range(1, 20):

	page = str(i)

	data = {
		'on': 'true',
		'page': page,
		'pageSize': '15',
		'productName': '',
		'conditionType': '1',
		'applyname': '',
		'applysn': '',
	}

	# getData(url, headers, data)
	# response = requests.post(url=url, headers=headers, data=data).json()
	# for dic in response['list']:
	# 	ids_list.append(dic['ID'])

	t = Thread(target=getData, args=(url, headers, data))
	t.start()
	task.append(t)

for i in task:
	i.join()

sub_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'

data_list = []

for i in ids_list:

	data_res = requests.post(url=sub_url, headers=headers, data={'id':i}).json()

	data_list.append(data_res)

fp = open('yjzj.json', 'w', encoding='utf-8')
json.dump(data_list, fp, ensure_ascii=False)
print('over')