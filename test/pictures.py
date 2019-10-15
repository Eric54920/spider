import requests
from lxml import etree

url = 'https://www.pexels.com/search/computer'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

res = requests.get(url=url, headers=headers).text
sub_res = etree.HTML(res)
img_divs = sub_res.xpath("//div[@class='l-container']/div[@class='photos']/div[@class='photos__column']/div")
# print(img_divs)
for div in img_divs:
    img_src = div.xpath('./article/a[1]/img/@src')[0]
    # print(img_src)
    if len(img_src) != '':
        img_name = img_src.split('?')[0].split('/')[5]
        print(img_name)
        img_data = requests.get(url=img_src, headers=headers).content
        with open(f'test/img/{img_name}','wb') as f:
            f.write(img_data)