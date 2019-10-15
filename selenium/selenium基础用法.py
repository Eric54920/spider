from selenium import webdriver
from lxml import etree
import time

# 实例化一个浏览器兑现（传入浏览器的驱动程序）
bro = webdriver.Chrome()
# 让浏览器发起一个指定url的请求
bro.get('http://125.35.6.84:81/xk')
# page_source获取浏览器当前页面的页面源码数据
page_text = bro.page_source
# 解析企业名称
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
	name = li.xpath('./dl/@title')[0]
	print(name)
time.sleep(5)
bro.quit()
