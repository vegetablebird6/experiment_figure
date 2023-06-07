from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate

#定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')

#定义三维数据
originTimeConsumpt = [
    [
        [1264,1108,1098,1092,1092,1103,1105,1101,1098,1095,1109,1186,1095,1098,1181,1103,1127,1208,1091,1093,1107,1097,1101,1092,1101,1106,1108,1100,1223,1101,1212,1097,1097,1190,1111,1103,1103,1091,1109,1094,1102,1097,1197,1098,1105,1107,1102,1101,1105,1097],
        [699,714,633,629,638,635,633,629,634,632,636,633,630,630,630,706,639,635,640,628,636,629,714,706,717,634,630,641,632,635,629,637,718,634,636,633,637,630,632,636,638,631,639,631,631,700,631,639,637,632],
        [432,438,436,439,432,435,436,435,431,432,439,434,436,435,431,435,431,433,437,517,437,438,435,437,432,436,434,438,433,431,431,511,434,435,933,436,437,433,435,433,436,514,437,434,439,432,439,437,438,434],
        [216,216,214,214,215,219,216,214,217,217,214,214,215,215,217,216,213,213,215,219,214,215,215,219,321,216,215,217,215,216,217,218,215,216,215,216,215,218,219,216,215,216,218,295,217,215,214,218,217,216]
    ],
    [
        [1589,1442,1416,1473,1504,1467,1447,1455,1452,1443,1558,1449,1434,1449,1456,1575,1467,1454,1468,1462,1452,1445,1473,1464,1417,1430,1435,1452,1442,1445,1469,1473,1434,1464,1472,1442,1562,1426,1448,1450,1460,1570,1417,1474,1464,1444,1449,1553,1428,1464],
        [792,711,716,722,713,728,712,719,795,721,723,715,722,718,710,710,722,710,711,713,775,710,719,711,719,712,711,720,707,711,718,718,711,712,719,722,720,711,718,713,719,710,722,709,716,711,719,720,776,709],
        [484,491,483,484,490,485,491,484,486,490,486,492,486,485,486,492,493,492,483,487,485,492,491,563,485,490,484,485,487,490,488,490,492,485,489,492,488,486,491,492,485,493,490,484,485,484,491,492,484,482],
        [269,266,272,266,270,271,271,271,270,268,267,269,268,266,271,267,269,272,266,267,265,265,271,267,270,271,270,268,267,265,268,267,271,266,268,270,271,268,268,270,270,269,267,271,267,268,271,271,270,266]
    ],
    [
        [1948,1977,1833,1838,1858,1756,1759,1767,1799,1858,1761,1793,1797,1792,1882,1764,1790,1790,1788,1793,1768,1794,1770,1801,1796,1792,1789,1766,1766,1763,1766,1900,1795,1792,1795,1797,1792,1787,1760,1800,1763,1909,1797,1851,1789,1799,1787,1886,1775,1767],
        [1019,940,956,962,959,941,942,1013,1041,942,958,965,954,941,942,943,940,944,945,941,966,962,966,959,963,943,945,1032,960,959,944,943,1029,1029,943,942,944,957,944,959,940,960,941,954,954,958,958,944,960,943],
        [631,632,646,634,633,633,642,645,630,646,644,647,632,646,640,633,632,714,645,641,634,642,634,642,643,637,631,630,642,640,634,641,708,643,643,644,639,644,638,631,645,642,641,633,644,643,643,636,643,646],
        [330,323,324,328,325,325,329,324,328,325,396,328,330,322,330,331,328,325,324,323,325,324,324,328,323,324,402,322,330,324,324,326,328,329,329,330,326,328,330,328,324,324,324,328,324,324,332,328,324,325]
    ],
    [
        [2307,2167,2208,2216,2207,2306,2168,2165,2294,2211,2212,2271,2167,2289,2176,2212,2279,2166,2174,2177,2210,2312,2206,2167,2310,2208,2179,2212,2171,2314,2166,2208,2310,2205,2203,2176,2163,2176,2208,2207,2215,2169,2174,2406,2314,2318,2161,2169,2213,2172],
        [1122,1050,1051,1077,1071,1069,1073,1069,1053,1074,1071,1069,1074,1039,1049,1068,1051,1071,1039,1055,1074,1143,1052,1077,1074,1069,1049,1067,1072,1070,1072,1039,1071,1035,1074,1057,1052,1073,1052,1037,1049,1054,1075,1042,1114,1039,1073,1068,1065,1058],
        [705,705,714,704,714,703,703,720,704,715,705,704,718,706,889,716,788,718,704,718,719,702,703,706,717,703,705,717,716,704,716,725,717,721,719,716,705,716,718,706,704,716,718,704,705,718,719,718,717,702],
        [330,323,324,328,325,325,329,324,328,325,396,328,330,322,330,331,328,325,324,323,325,324,324,328,323,324,402,322,330,324,324,326,328,329,329,330,326,328,330,328,324,324,324,328,324,324,332,328,324,325]
    ],
    [
        [2653,2655,2599,2766,2600,2601,2746,2652,2601,2792,2644,2767,2592,2597,2703,2651,2645,2594,2595,2941,2664,2771,2591,2602,2711,2654,2596,2657,2597,2825,2642,2606,2727,2602,2649,2654,2606,2598,2648,2597,2930,2599,2730,2651,2650,2757,2639,2602,2752,2642],
        [1344,1404,1323,1323,1324,1325,1338,1327,1317,1318,1359,1323,1322,1318,1320,1317,1318,1317,1324,1325,1323,1318,1320,1327,1398,1327,1318,1318,1467,1318,1325,1323,1399,1316,1318,1323,1344,1325,1324,1317,1448,1316,1326,1328,1410,1326,1324,1324,1456,1338],
        [895,968,896,892,906,892,895,896,892,893,892,893,969,893,907,892,908,977,892,974,892,895,890,891,891,906,908,891,892,892,895,902,907,961,907,978,890,910,894,894,904,899,904,897,891,906,909,890,896,895],
        [471,465,471,464,462,471,463,462,463,470,462,461,471,473,471,463,472,472,464,471,463,464,462,464,471,462,472,462,463,463,463,472,472,470,463,474,463,465,474,471,463,461,472,473,464,472,463,463,474,473]
    ]
]

processTimeConsumpt = [
   [np.mean(j) for j in i] for i in originTimeConsumpt
]

# frequency = [200, 400, 600, 1200]
# number = [10, 20, 30, 40, 50]
# X, Y = np.meshgrid(frequency, number)
# Z = np.array(processTimeConsumpt)

frequency = np.array([200, 400, 600, 1200])
number = np.array([10, 20, 30, 40, 50])
result = np.array([processTimeConsumpt])
# 插值
f = interpolate.interp2d(frequency, number, result, kind='cubic')
newfrequency = np.linspace(200, 1200, 1001)
newnumber = np.linspace(10, 50, 41)
Z = f(newfrequency, newnumber)

X, Y = np.meshgrid(newfrequency, newnumber)

#作图
ax1.set_xlabel('Frequency')
ax1.set_ylabel('ID')
ax1.set_zlabel('Time')
ax1.plot_surface(X,Y,Z)
plt.show()