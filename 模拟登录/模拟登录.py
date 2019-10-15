import requests
from lxml import etree
import fateadm_api

app_id = '316378'
app_key = 'LQ+cGEvrbHWUDQH9CsrBKBSrIfOer2lk'
pd_id = '116378'
pd_key = 'M2LzNpl7evt2w87Squah0YK/psWFxdRj'
url = 'http://www.renren.com/SysHome.do'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}
# 创建session对象
session = requests.Session()

# 获取验证码
res = requests.get(url=url, headers=headers).text
tree = etree.HTML(res)
img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
img_data = requests.get(url=img_src, headers=headers).content
with open('./code_img.jpg', 'wb') as f:
	f.write(img_data)


fateadm = fateadm_api.FateadmApi(app_id, app_key, pd_id, pd_key)
# 接收验证码结果
code = fateadm.PredictFromFile(30600, './code_img.jpg')

# 模拟登录
login_url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=201983124674'
data = {
	'email': '15110962402',
	'icode': code.pred_rsp.value,
	'origURL': 'http://www.renren.com/home',
	'domain': 'renren.com',
	'key_id': '1',
	'captcha_type': 'web_login',
	'password': '0d55d950b620bd6d6bfc7825ba28d009f34bfe748f0db1353937ad5087000a83',
	'rkey': 'c177ee12a58da2b2d83a728d1ecb1c73',
	'f': ''
}
res = session.post(url=login_url, headers=headers, data=data)
print(res.status_code)
if res.status_code == 200:
	home_page = session.get(url='http://www.renren.com/972145644/newsfeed/photo', headers=headers).text
	with open('./home_page.html', 'w', encoding='utf-8') as f:
		f.write(home_page)
	profile = session.get(url='http://www.renren.com/972145644/profile', headers=headers).text
	with open('./profile.html', 'w', encoding='utf-8') as f1:
		f1.write(profile)
else:
	fateadm.Justice(code.request_id)

