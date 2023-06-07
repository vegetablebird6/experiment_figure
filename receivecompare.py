import matplotlib.pyplot as plt
import numpy as np
# 读取数据
# data = [[271,271,268,273,261,256,275,260,264,267,261,284,277,270,259,269,282,275,288,281,275,268,265,268,269,272,264,271,276,277,268,267,261,272,270,268,268,286,267,265,266,261,265,267,279,265,268,266,417,419],
#         [194,194,203,202,202,203,198,195,191,206,203,197,208,208,207,200,201,204,211,198,210,203,205,192,200,203,207,207,205,207,203,208,208,204,193,189,191,198,192,196,197,207,193,199,196,196,188,189,255,253],
#         [149,140,139,136,137,134,133,137,139,145,135,139,133,132,140,136,148,140,136,157,144,135,147,171,147,139,136,136,141,148,140,139,142,138,142,138,139,143,138,144,149,140,144,138,147,141,141,141,169,147],
#         [74, 81, 73, 67, 68, 68, 63, 73, 73, 78, 73, 71, 68, 79, 81, 84, 68, 74, 79, 71, 74, 102, 78, 72, 83, 76, 81, 72, 78, 78, 73, 79, 78, 78, 105, 75, 86, 78, 84, 76, 74, 74, 74, 70, 71, 73, 68, 80, 77, 69]
#         ]
data = [[271,271,268,273,261,256,275,260,264,267,261,284,277,270,259,269,282,275,288,281,275,268,265,268,269,272,264,271,276,277,268,267,261,272,270,268,268,286,267,265,266,261,265,267,279,265,268,266,282,279],
        [194,194,203,202,202,203,198,195,191,206,203,197,208,208,207,200,201,204,211,198,210,203,205,192,200,203,207,207,205,207,203,208,208,204,193,189,191,198,192,196,197,207,193,199,196,196,188,189,195,193],
        [149,140,139,136,137,134,133,137,139,145,135,139,133,132,140,136,148,140,136,147,144,135,147,141,147,139,136,136,141,148,140,139,142,138,142,138,139,143,138,144,149,140,144,138,147,141,141,141,139,147],
        [74, 81, 73, 67, 68, 68, 63, 73, 73, 78, 73, 71, 68, 79, 81, 84, 68, 74, 79, 71, 74, 72, 78, 72, 83, 76, 81, 72, 78, 78, 73, 79, 78, 78, 75, 75, 86, 78, 84, 76, 74, 74, 74, 70, 71, 73, 68, 80, 77, 69]
        ]

newData = [[j / 1000 for j in i] for i in data]
fig = plt.figure()
plt.rcParams['xtick.labelsize'] = 13  # x 轴刻度标签的字体大小
plt.rcParams['ytick.labelsize'] = 13  # y 轴刻度标签的字体大小
labels = '200 (RPi)','400 (RPi)','600 (RPi)','1200 (T-Box)'
plt.xlabel('CPU frequency (MHz)',fontsize=13)
plt.ylabel('Time (ms)',fontsize=13)
plt.boxplot(newData, labels=labels)  # grid=False：代表不显示背景中的网格线
fig.savefig('./receive.pdf',dpi=600,format='pdf',bbox_inches='tight')
plt.show()  # 显示图像
print(np.mean(data[3]))