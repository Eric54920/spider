import asyncio

async def requests(url):
	print(f'正在请求的url:{url}')
	print(f'请求成功:{url}')
	return url
# 被async修饰的函数，被调用后返回一个协程对象
c = requests('www.baidu.com')

# 创建一个时间循环对象
# loop = asyncio.get_event_loop()
# 将协程对象注册到loop对象中，然后启动loop
# loop.run_until_complete(c)


# task的使用
# loop = asyncio.get_event_loop()
# 基于loop创建一个任务
# task = loop.create_task(c)
# print(task)
# loop.run_until_complete(task)
# print(task)


# future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)


# 绑定回调
# def call_back(task):
# 	print(task.result())
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# task.add_done_callback(call_back)
# loop.run_until_complete(task)


