import chaojiying
from selenium import webdriver
from selenium.webdriver import ActionChains
from PIL import Image
import time

url = 'https://kyfw.12306.cn/otn/resources/login.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

bro = webdriver.Chrome()
bro.get(url)
time.sleep(5)
login_btn = bro.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]')
login_btn.click()
# 将当前页面进行截图保存
bro.save_screenshot('a.png')
# 确定验证码图片的坐标
code_img_ele = bro.find_element_by_xpath('//*[@id="J-loginImg"]')
# 验证码图片左上角的x,y
location = code_img_ele.location
print(location)
# 验证码图片的尺寸
size = code_img_ele.size
print(size)
# 左上角和右上角的坐标
rangle = (int(location['x']), int(location['y']), int(location['x']+size['width']), int(location['y']+size['height']))
print(rangle)
i = Image.open('./a.png')
code_img_name = './code.png'
frame = i.crop(rangle)
frame.save(code_img_name)

chaojiying = chaojiying.Chaojiying_Client('Eric54920', 'Eric54920!', '901421')
im = open('code.png', 'rb').read()
ret = chaojiying.PostPic(im, 9004)

if ret['err_str'] == 'OK':
    result = ret['pic_str']
else:
    chaojiying.ReportError(ret['pic_id'])

all_list = []
if '|' in result:
    list = result.split('|')
    for i in range(len(list)):
        xy_list = []
        x = int(list[i].split(',')[0])
        y = int(list[i].split(',')[1])
        xy_list.append(x)
        xy_list.append(y)
        all_list.append(xy_list)
else:
    x = int(result.split(',')[0])
    y = int(result.split(',')[1])
    all_list.append(x)
    all_list.append(y)
print(all_list)
for i in all_list:
    x = i[0]
    y = i[1]
    ActionChains(bro).move_to_element_with_offset(code_img_ele, x, y).click().perform()
    time.sleep(0.5)

bro.find_element_by_id('username').end.keys('1234567')
time.sleep(3)
bro.find_element_by_id('password').end.keys('*******')
time.sleep(3)
bro.find_element_by_id('login_Sub').click()
time.sleep(3)
bro.quit()