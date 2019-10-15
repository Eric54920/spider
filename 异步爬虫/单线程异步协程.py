import requests
import aiohttp
import asyncio
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

start = time.time()
async def get_page(url):
	async with aiohttp.ClientSession() as session:
		# get(),post()
		# headers, params/data, proxy='https://ip:port'
		async with await session.get(url, headers=headers) as response:
			# text():返回字符串形式的响应数据
			# read():返回二进制形式的响应数据
			# json():返回json形式的响应数据
			page_text = await response.text()
			print(page_text)

urls = ['http://www.baidu.com', 'http://www.zhihu.com', 'http://www.ithome.com']

tasks = []

loop = asyncio.get_event_loop()
for url in urls:
	c = get_page(url)
	task = loop.create_task(c)
	tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))

print(f'用时：{time.time() - start}')
