import asyncio
import time

async def requests(url):
	print(f'正在请求：{url}')
	await asyncio.sleep(2)
	print(f'请求完成：{url}')

urls = ['www.baidu.com', 'www.google.com', 'www.bing.com']

tasks = []

loop = asyncio.get_event_loop()
start_time = time.time()

for url in urls:
	c = requests(url)
	task = loop.create_task(c)
	# 或 # tsak = asyncio.ensure_future(c)
	tasks.append(task)

loop.run_until_complete(asyncio.wait(tasks))
print(time.time() - start_time)