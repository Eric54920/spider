import pygal
from functools import reduce

with open('spider/test/chou.csv', 'r', encoding='utf-8') as f:
    data = f.readlines()
total_money = []
curr_money = []
for i in data:
    i = i.split(',')
    if i[1].isdecimal():
        total_money.append(int(i[1]))
        curr_money.append(float(i[2]))
    else:
        continue

chart = pygal.Line()
chart.title = '总金额分布图'
chart.x_labels = map(str, range(1, 101))
chart.add('总金额', total_money)
chart.add('已筹金额', curr_money)
chart.render_to_file('总金额.svg')

total_money.sort()

print('中位数：',(total_money[50]+total_money[51])/2)
print('最大值：', max(total_money))
print('最小值：', min(total_money))
print('平均值：', reduce(lambda x,y:x+y, total_money)/len(total_money))