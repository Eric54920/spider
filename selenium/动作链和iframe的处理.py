from selenium import webdriver
from selenium.webdriver import ActionChains
import time

bro = webdriver.Chrome(executable_path='./chromedriver')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# 如果定位的标签是存在于iframe中，则通过如下操作进行标签定位
bro.switch_to.frame('iframeResult')
div = bro.find_element_by_id('draggable')

# 动作链
action = ActionChains(bro)
# 点击长按div
action.click_and_hold(div)
for i in range(5):
	# perform():立即执行动作链操作
	# move_by_offset(x, y):向水平和竖直方向移动
	action.move_by_offset(17, 0).perform()
	time.sleep(0.3)

action.release()
bro.quit()