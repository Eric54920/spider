from selenium import webdriver
from selenium.webdriver import ActionChains
import time
bro = webdriver.Chrome()
# 实例化浏览器对象
# 发送请求
bro.get('https://qzone.qq.com')
# 定位账号密码登录链接
bro.switch_to.frame('login_frame')
btn = bro.find_element_by_xpath('//*[@id="switcher_plogin"]')
time.sleep(2)
btn.click()

# 定位到账号数据框
user_inp = bro.find_element_by_xpath('//*[@id="u"]')
user_inp.send_keys('11789014')
# 定位到密码输入框
pwd_inp = bro.find_element_by_xpath('//*[@id="p"]')
pwd_inp.send_keys('Eric54920!')
# 定位到登录按钮
login_btn = bro.find_element_by_xpath('//*[@id="loginform"]/div[4]')
# 点击登录按钮
login_btn.click()

page_source = bro.page_source()

print(page_source)
