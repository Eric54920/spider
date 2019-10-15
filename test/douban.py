import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0'
}

for i in range(2):
    url = f'https://movie.douban.com/subject/30295905/comments?start={i*20}&limit=20&sort=time&status=P&percent_type='

    res = requests.get(url=url, headers=headers).text
    sub_res = etree.HTML(res)
    div_list = sub_res.xpath("//*[@id='comments']/div[@class='comment-item']")
    # fp = open('test/comment.csv', 'w', encoding='utf-8')
    fp = open('test/comment.txt', 'w', encoding='utf-8')
    fp.write('comment'+'\n')
    for div in div_list:
        info = div.xpath('./div[2]/p/span/text()')[0]
        fp.write(info+'\n')
        print(info)