import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import numpy as np

x = [10,20,30,40,50]

y1 = [8.4366, 16.7756, 24.994, 33.528800000000004, 41.349999999999994]
y2 = [10.603000000000002, 21.03, 31.468, 41.895, 52.333000000000006]
y3 = [480,770,1200,1550,2000]

fig=plt.figure()
plt.rcParams['xtick.labelsize'] = 13  # x 轴刻度标签的字体大小
plt.rcParams['ytick.labelsize'] = 13  # y 轴刻度标签的字体大小
left,bottom,width,height=0.13,0.1,0.8,0.8
ax1=fig.add_axes([left,bottom,width,height])
ax1.plot(x, y1, label='LCCKE',marker='s')  # 绘制第一条折线
ax1.plot(x, y2, label='CIST',marker='v')  # 绘制第二条折线
ax1.plot(x, y3, label='FEKE_main',marker='o')  # 绘制第三条折线
ax1.set_xlabel("Number of ECUs",fontsize=13)             #设置x，y轴的标签
ax1.set_ylabel("Time (ms)",fontsize=13)
ax1.legend()

left,bottom,width,height=0.52,0.205,0.35,0.35
ax2=fig.add_axes([left,bottom,width,height])
ax2.plot(x, y1, label='LCCKE',marker='s')  # 绘制第一条折线
ax2.plot(x, y2, label='CIST',marker='v')  # 绘制第二条折线
fig.savefig('./LCCKEsolutioncompare.eps',dpi=600,format='eps',bbox_inches='tight')
plt.show()


# # 导入matplotlib库
# import matplotlib.pyplot as plt
# # 导入numpy库
# import numpy as np
#
# # 定义数据列表
# y1 = [8.4366, 16.7756, 24.994, 33.528800000000004, 41.349999999999994]
# y2 = [10.603000000000002, 21.03, 31.468, 41.895, 52.333000000000006]
# y3 = [480,770,1200,1550,2000]
#
# fig, ax = plt.subplots()
#
# # 定义柱状图的宽度
# width = 0.5
#
# # 定义x轴的标签
# labels = ['10','20','30','40','50']
#
# # 创建x轴的位置数组
# x = np.arange(len(labels))
#
#
# # 绘制三组柱状图，分别使用不同的颜色和图案
# ax.bar(x - width/3, y1, width/3, label="LCCKE")
# ax.bar(x, y2, width/3, label="CIST")
# ax.bar(x + width/3, y3, width/3, label="FEKE_main")
# # plt.bar(x3, data3, width, color="white", label="data3", edgecolor="black", hatch="xxx")
#
# # 设置x轴的刻度和标签
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# # 设置x轴的标签
# ax.set_xlabel("Number of ECUs",fontsize=13)
#
# # 设置y轴的标签
# ax.set_ylabel("Time (ms)",fontsize=13)
#
# # 显示图例
# ax.legend()
#
# # 显示图表
# plt.show()
#
# fig.savefig('./LCCKEsolutioncompare.eps',dpi=600,format='eps',bbox_inches='tight')

# import matplotlib.pyplot as plt
# import numpy as np
# fig, ax = plt.subplots()
# labels = ['10','20','30','40','50']
#
# x = [10,20,30,40,50]
# # y1 = [2.8,5.6,8.4,11.2,14]
# y1 = [8.4366, 16.7756, 24.994, 33.528800000000004, 41.349999999999994]
# y2 = [10.603000000000002, 21.03, 31.468, 41.895, 52.333000000000006]
# y3 = [480,770,1200,1550,2000]
#
# ax.plot(x, y1, label='LCCKE',marker='s')  # 绘制第一条折线
# ax.plot(x, y2, label='CIST',marker='v')  # 绘制第二条折线
# ax.plot(x, y3, label='FEKE_main',marker='^')  # 绘制第三条折线
# # 可以添加更多的绘制语句
#
# ax.set_xlabel('Number of ECUs',fontsize=13)  # 设置 x 轴标签
# ax.set_ylabel('Time (ms)',fontsize=13)  # 设置 y 轴标签
# ax.legend()  # 显示图例
# ax.set_xticks(x)
# ax.xaxis.set_tick_params(labelsize=13)
# ax.yaxis.set_tick_params(labelsize=13)
# fig.savefig('./LCCKEsolutioncompare.eps',dpi=600,format='eps',bbox_inches='tight')
# plt.show()  # 显示图表
