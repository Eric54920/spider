import requests
import json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}
json_list = []
for i in range(8):
    param = {
        'cname': '北京',
        'pid': '13',
        'pageIndex': i+1,
        'pageSize': '10'
    }
    response = requests.get(url=url,headers=headers, params=param)
    json_list.append(response.json())
with open('kfc.json', 'w', encoding='utf-8')as f:
    json.dump(json_list, f, ensure_ascii=False)