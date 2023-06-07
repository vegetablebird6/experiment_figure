# import matplotlib.pyplot as plt
# import numpy as np
#
# labels = ['10','20','30','40','50']
#
# y1 = [11,21,31,41,51]
# y2 = [30,60,90,120,150]
# y3 = [(i+1) * 10 * 64  for i in range(5)]
# y4 = [(i+1) * 10 * 32  for i in range(5)]
# y5 = [(i+1) * 10 * 44  for i in range(5)]
#
# newy1 = [i/4000 for i in y1]
# newy2 = [i/4000 for i in y2]
# newy3 = [i/4000 for i in y3]
# newy4 = [i/4000 for i in y4]
# newy5 = [i/4000 for i in y5]
# print(newy1)
# print(newy2)
# print(newy3)
# print(newy4)
# print(newy5)
# x = np.arange(len(labels))
# width = 0.5
# fig, ax = plt.subplots()
#
# rects1 = ax.bar(x - 2*width/5, newy1, width/5, label='LCCKE')
# rects2 = ax.bar(x - width/5, newy2, width/5, label='CIST')
# rects3 = ax.bar(x, newy3, width/5, label='FEKE_main')
# rects4 = ax.bar(x + width/5, newy4, width/5, label='FEKE_sym')
# rects5 = ax.bar(x + 2*width/5, newy5, width/5, label='FEKE_wlo')
# # rects4 = ax.bar(x + 3*width/8, HMAC_SHA3_256, width/4, label='HMAC-SHA3-256',color='k')
# # Add some text for labels, title and custom x-axis tick labels, etc.
#
# ax.set_xlabel('Number of ECUs')
# ax.set_ylabel('Bus Load (%)')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()
#
# fig.savefig('./LCCKEloadcompare.eps',dpi=600,format='eps')
# plt.show()

# 导入matplotlib库
import matplotlib.pyplot as plt
# 导入numpy库
import numpy as np

# 定义数据列表
y1 = [11,21,31,41,51]
y2 = [30,60,90,120,150]
y3 = [(i+1) * 10 * 64  for i in range(5)]
y4 = [(i+1) * 10 * 32  for i in range(5)]
y5 = [(i+1) * 10 * 44  for i in range(5)]

newy1 = [i/4000 for i in y1]
newy2 = [i/4000 for i in y2]
newy3 = [i/4000 for i in y3]
newy4 = [i/4000 for i in y4]
newy5 = [i/4000 for i in y5]

fig, ax = plt.subplots()

# 定义柱状图的宽度
width = 0.5

# 定义x轴的标签
labels = ['10','20','30','40','50']

# 创建x轴的位置数组
x = np.arange(len(labels))


# 绘制三组柱状图，分别使用不同的颜色和图案
rects1 = ax.bar(x - 2*width/5, newy1, width/5, label='LCCKE')
rects2 = ax.bar(x - width/5, newy2, width/5, label='CIST')
rects3 = ax.bar(x, newy3, width/5, label='FEKE_main')
rects4 = ax.bar(x + width/5, newy4, width/5, label='FEKE_sym')
rects5 = ax.bar(x + 2*width/5, newy5, width/5, label='FEKE_wlo')


# 设置x轴的刻度和标签
ax.set_xticks(x)
ax.set_xticklabels(labels)
# 设置x轴的标签
ax.set_xlabel("Number of ECUs",fontsize=13)

# 设置y轴的标签
ax.set_ylabel("Bus Load (%)",fontsize=13)

# 显示图例
ax.legend()

# 显示图表
plt.show()

fig.savefig('./LCCKEloadcompare.eps',dpi=600,format='eps',bbox_inches='tight')