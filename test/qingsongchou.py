import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

fp = open('chou.csv', 'a', encoding='utf-8')
head = "序号,目标金额,已筹集额,捐赠人数,转发数量,发布日期"
fp.write(head+'\n')
count = 1

for j in range(1, 6):
    url = f'https://partner-gateway.qschou.com/official/pc/project/succeed?page={j}'
    res = requests.get(url=url, headers=headers).json()
    for i in res['data']:
        channel = i['channel']
        raisefund_no = i['raisefund_no']
        detail_url = f'https://partner-gateway.qschou.com/{channel}/project/{raisefund_no}/info'
        res_sub = requests.get(url=detail_url, headers=headers).json()

        total_money = res_sub['data']['total_amount']
        curr_money = res_sub['data']['current_amount']
        dom_num = res_sub['data']['backer_count']
        share_num = res_sub['data']['share_count']
        pub_date = raisefund_no[0:8]
        data = f'{count},{total_money},{curr_money},{dom_num},{share_num},{pub_date}'
        count += 1
        fp.write(data+'\n')