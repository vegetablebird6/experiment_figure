from matplotlib import pyplot as plt
import numpy
import random

# data = [
#     [783,823,795,785,783,777,774,773,797,783,773,787,767,784,808,773,773,802,793,780,787,777,778,778,774,773,776,929,786,774,774,773,780,782,861,775,782,779,780,769,787,893,786,771,778,611,585,812,573,582],
#     [331,304,297,291,294,314,305,341,290,293,291,300,303,294,293,291,294,291,293,291,339,329,299,288,301,357,323,296,292,293,291,305,296,303,289,299,293,293,292,290,311,300,298,292,305,295,297,312,364,309],
#     [273,278,278,272,275,282,223,209,212,212,202,219,206,205,204,204,201,215,206,215,202,239,218,266,266,270,266,270,269,267,267,269,265,265,268,270,270,269,266,267,267,268,265,263,270,269,271,268,266,269],
#     [149,144,142,142,149,143,150,142,144,144,145,149,143,143,143,141,142,143,142,151,142,154,145,146,141,141,141,145,142,145,143,151,146,145,139,142,140,141,139,168,147,151,147,146,148,143,154,148,153,149]
# ]
origin = [783,823,735,745,743,737,754,753,757,743,733,747,767,744,808,723,723,702,713,740,717,727,738,778,774,773,776,729,786,774,774,773,780,782,761,775,782,779,780,769,787,793,786,771,778,711,685,812,773,682]
data = []
mac_time = 150
trans_time = 70
for k in range(5):
    temp = []
    for j in range(50):
        temp.append(origin[random.randint(0,49)] * (k+1)*10  + ((k+1)*10+1)*trans_time + mac_time)
    data.append(temp)
newData = [[j / 1000 for j in i] for i in data]
print([numpy.mean(i) for i in newData])
fig = plt.figure()
labels = '10','20','30','40', '50'
plt.rcParams['xtick.labelsize'] = 13  # x 轴刻度标签的字体大小
plt.rcParams['ytick.labelsize'] = 13  # y 轴刻度标签的字体大小
plt.xlabel('Number of ECUs',fontsize=13)
plt.ylabel('Time (ms)',fontsize=13)
plt.boxplot(newData, labels=labels)  # grid=False：代表不显示背景中的网格线
fig.savefig('./LCCKEmutilecu.eps',dpi=600,format='eps',bbox_inches='tight')
plt.show()  # 显示图像