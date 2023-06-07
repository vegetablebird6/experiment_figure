# import matplotlib.pyplot as plt
# import numpy as np
# labels = ['10','20','30','40','50']
# y1 = [8.4366, 16.7756, 24.994, 33.528800000000004, 41.349999999999994]
# y2 = [10.603000000000002, 21.03, 31.468, 41.895, 52.333000000000006]
#
# x = np.arange(len(labels))
# width = 0.4
# fig, ax = plt.subplots()
#
# rects1 = ax.bar(x - width/4, y1, width/2, label='LCCKE')
# rects3 = ax.bar(x + width/4, y2, width/2, label='CIST')
# # rects4 = ax.bar(x + 3*width/8, HMAC_SHA3_256, width/4, label='HMAC-SHA3-256',color='k')
# # Add some text for labels, title and custom x-axis tick labels, etc.
#
# ax.set_xlabel('Number of ECUs')
# ax.set_ylabel('time (ms)')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()
#
# fig.savefig('./LCCKEvsAEKP2.eps',dpi=600,format='eps')
# plt.show()


# # 导入matplotlib库
# import matplotlib.pyplot as plt
# # 导入numpy库
# import numpy as np
#
# # 定义数据列表
# y1 = [8.4366, 16.7756, 24.994, 33.528800000000004, 41.349999999999994]
# y2 = [10.603000000000002, 21.03, 31.468, 41.895, 52.333000000000006]
#
# fig, ax = plt.subplots()
#
# # 定义柱状图的宽度
# width = 0.4
#
# # 定义x轴的标签
# labels = ['10','20','30','40','50']
#
# # 创建x轴的位置数组
# x = np.arange(len(labels))
#
#
# # 绘制三组柱状图，分别使用不同的颜色和图案
# ax.bar(x - width/4, y1, width/2, label="LCCKE")
# ax.bar(x + width/4, y2, width/2, label="CIST")
# # plt.bar(x2, data2, width, color="white", label="data2", edgecolor="black", hatch="///")
# # plt.bar(x3, data3, width, color="white", label="data3", edgecolor="black", hatch="xxx")
#
# # 设置x轴的刻度和标签
# ax.set_xticks(x)
#
# # 设置x轴的标签
# ax.set_xlabel("Number of ECUs",fontsize=13)
# ax.set_xticklabels(labels)
# # 设置y轴的标签
# ax.set_ylabel("Time (ms)",fontsize=13)
#
# # 显示图例
# ax.legend()
#
# # 显示图表
# plt.show()
#
# fig.savefig('./LCCKEvsAKEP2.eps',dpi=600,format='eps',bbox_inches='tight')

import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
labels = ['10','20','30','40','50']

x = [10,20,30,40,50]
# y1 = [2.8,5.6,8.4,11.2,14]
y1 = [8.4366, 16.7756, 24.994, 33.528800000000004, 41.349999999999994]
y2 = [10.603000000000002, 21.03, 31.468, 41.895, 52.333000000000006]

ax.plot(x, y1, label='LCCKE',marker='s')  # 绘制第一条折线
ax.plot(x, y2, label='CIST',marker='v')  # 绘制第二条折线
# 可以添加更多的绘制语句

ax.set_xlabel('Number of ECUs',fontsize=13)  # 设置 x 轴标签
ax.set_ylabel('Time (ms)',fontsize=13)  # 设置 y 轴标签
ax.legend()  # 显示图例
ax.set_xticks(x)
ax.xaxis.set_tick_params(labelsize=13)
ax.yaxis.set_tick_params(labelsize=13)
fig.savefig('./LCCKEvsAKEP2.eps',dpi=600,format='eps',bbox_inches='tight')
plt.show()  # 显示图表