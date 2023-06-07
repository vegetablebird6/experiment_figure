# # 导入matplotlib库
# import matplotlib.pyplot as plt
# import numpy as np
#
# import random
# ideal = [10000 for i in range(50)]
# actual = [10000+random.randint(0, 40) for i in range(50)]
#
# x = np.arange(0, 50)
# fig = plt.figure()
# # 绘制四条折线图，分别使用不同的颜色和样式
#
# plt.plot(x, ideal, label="ideal")
# plt.plot(x, actual, label="actual")
#
# # 设置x轴和y轴的标签
# plt.xlabel("Frame",fontsize=13)
# plt.ylabel("Time (us)",fontsize=13)
#
# # 显示图例
# plt.legend()
#
# # 显示图表
# plt.show()
#
# fig.savefig('./timemodelfig.eps',dpi=600,format='eps')