from selenium import webdriver
from time import sleep

bro = webdriver.Chrome()
bro.get('https://www.taobao.com')
search_inp = bro.find_element_by_id('q')
search_inp.send_keys('墨镜')
bro.execute_script('window.scrollTo(0, document.body.scrollHeight)')
sleep(2)
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()
bro.get('https://www.baidu.com')
sleep(2)
# 回退
bro.back()
sleep(2)
bro.forward()
sleep(2)
bro.quit()