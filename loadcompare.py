# import matplotlib.pyplot as plt
# import numpy as np
#
# labels = ['5','10','15','20','25']
#
# # y1 = [2.8,5.6,8.4,11.2,14]
# y2 = [4,8,12,16,20]
# y3 = [4.4,8.8,13.2,17.6,22]
# y4 = [3.6,7.2,10.8,14.4,18]
#
#
# x = np.arange(len(labels))
# width = 0.4
# fig, ax = plt.subplots()
#
# # rects1 = ax.bar(x - 3*width/8, y1, width/4, label='Origin CAN', color="black")
# # rects2 = ax.bar(x - width/8, y2, width/4, label='MTDCAP', color="white", edgecolor="black")
# # rects3 = ax.bar(x + width/8, y3, width/4, label='CIST', color="white", edgecolor="black", hatch="ooo")
# # rects4 = ax.bar(x + 3*width/8, y4, width/4, label='Mini-MAC', color="white", edgecolor="black", hatch="///")
# # rects1 = ax.bar(x - 3*width/8, y1, width/4, label='Origin CAN')
# # rects2 = ax.bar(x - width/8, y2, width/4, label='MTDCAP')
# # rects3 = ax.bar(x + width/8, y3, width/4, label='CIST')
# # rects4 = ax.bar(x + 3*width/8, y4, width/4, label='Mini-MAC')
# rects2 = ax.bar(x - width/3, y2, width/3, label='MTDCAP')
# rects3 = ax.bar(x, y3, width/3, label='Mini-MAC')
# rects4 = ax.bar(x + width/3, y4, width/3, label='CIST')
#
#
# ax.set_xlabel('Number of ECUs')
# ax.set_ylabel('Bus load (%)')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()
#
# fig.savefig('./loadcompare.pdf',dpi=600,format='pdf')
# plt.show()
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()
labels = ['5','10','15','20','25']

x = [5,10,15,20,25]
# y1 = [2.8,5.6,8.4,11.2,14]
y2 = [4,8,12,16,20]
y3 = [4.4,8.8,13.2,17.6,22]
y4 = [3.6,7.2,10.8,14.4,18]

ax.plot(x, y2, label='MTDCAP',marker='s')  # 绘制第一条折线
ax.plot(x, y3, label='Mini-MAC',marker='o')  # 绘制第二条折线
ax.plot(x, y4, label='CIST',marker='^')  # 绘制第二条折线
# 可以添加更多的绘制语句

ax.set_xlabel('Number of ECUs',fontsize=13)  # 设置 x 轴标签
ax.set_ylabel('Bus load (%)',fontsize=13)  # 设置 y 轴标签
ax.legend()  # 显示图例
ax.set_xticks(x)
ax.xaxis.set_tick_params(labelsize=13)
ax.yaxis.set_tick_params(labelsize=13)
fig.savefig('./loadcompare.pdf',dpi=600,format='pdf',bbox_inches='tight')
plt.show()  # 显示图表