import matplotlib.pyplot as plt

# 读取数据
data = [[1122,1114,1107,1059,1079,1104,1144,1111,1095,1091,1080,1116,1060,1101,1081,1099,1089,1116,1112,1088,1151,1080,1112,1113,1078,1061,1080,1115,1087,1113,1135,1110,1111,1085,1101,1086,1094,1087,1057,1114,1062,1092,1114,1088,1080,1083,1086,1092,1083,1085],
        [1591,1505,1486,1492,1491,1511,1485,1586,1593,1494,1491,1483,1489,1479,1513,1648,1492,1584,1593,1646,1481,1495,1506,1481,1510,1494,1498,1596,1483,1644,1484,1476,1482,1481,1479,1485,1481,1597,1481,1482,1482,1481,1510,1515,1493,1518,1589,1623,1592,1494],
        [2180,2179,2095,2177,2176,2178,2092,2096,2099,2180,2193,2082,2080,2081,2093,2079,2096,2078,2097,2064,2093,2077,2076,2158,2182,2192,2154,2171,2081,2077,2093,2065,2093,2079,2080,2078,2078,2092,2074,2070,2082,2161,2080,2096,2077,2078,2065,2076,2097,2064]
        ]
newData = [[j / 1000 for j in i] for i in data]
fig = plt.figure()
labels = 'SHA-2','BLAKE2s','SHA-3'
plt.rcParams['xtick.labelsize'] = 13  # x 轴刻度标签的字体大小
plt.rcParams['ytick.labelsize'] = 13  # y 轴刻度标签的字体大小
plt.ylabel('Time (ms)',fontsize=13)
plt.boxplot(newData, labels=labels)  # grid=False：代表不显示背景中的网格线
fig.savefig('./genHCcompare.eps',dpi=600,format='eps',bbox_inches='tight')
plt.show()  # 显示图像