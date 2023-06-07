import random

import numpy

# initData = [2033,2158,2214,2155,2163,2154,2161,2035,2156,2180,2033,2158,2214,2155,2163,2154,2161,2035,2156,2180,2033,2158,2214,2155,2163,2154,2161,2035,2156,2180,2033,2158,2214,2155,2163,2154,2161,2035,2156,2180,2033,2158,2214,2155,2163,2154,2161,2035,2156,2180]
#
# genID = [
#     [1264,1108,1098,1092,1092,1103,1105,1101,1098,1095,1109,1186,1095,1098,1181,1103,1127,1208,1091,1093,1107,1097,1101,1092,1101,1106,1108,1100,1223,1101,1212,1097,1097,1190,1111,1103,1103,1091,1109,1094,1102,1097,1197,1098,1105,1107,1102,1101,1105,1097],
#     [1589,1442,1416,1473,1504,1467,1447,1455,1452,1443,1558,1449,1434,1449,1456,1575,1467,1454,1468,1462,1452,1445,1473,1464,1417,1430,1435,1452,1442,1445,1469,1473,1434,1464,1472,1442,1562,1426,1448,1450,1460,1570,1417,1474,1464,1444,1449,1553,1428,1464],
#     [1948,1977,1833,1838,1858,1756,1759,1767,1799,1858,1761,1793,1797,1792,1882,1764,1790,1790,1788,1793,1768,1794,1770,1801,1796,1792,1789,1766,1766,1763,1766,1900,1795,1792,1795,1797,1792,1787,1760,1800,1763,1909,1797,1851,1789,1799,1787,1886,1775,1767],
#     [2307,2167,2208,2216,2207,2306,2168,2165,2294,2211,2212,2271,2167,2289,2176,2212,2279,2166,2174,2177,2210,2312,2206,2167,2310,2208,2179,2212,2171,2314,2166,2208,2310,2205,2203,2176,2163,2176,2208,2207,2215,2169,2174,2406,2314,2318,2161,2169,2213,2172],
#     [2653,2655,2599,2766,2600,2601,2746,2652,2601,2792,2644,2767,2592,2597,2703,2651,2645,2594,2595,2941,2664,2771,2591,2602,2711,2654,2596,2657,2597,2825,2642,2606,2727,2602,2649,2654,2606,2598,2648,2597,2930,2599,2730,2651,2650,2757,2639,2602,2752,2642]
# ]
#
# send = [718,714,714,713,721,718,721,727,729,733,710,709,712,728,718,709,755,731,774,749,799,757,730,754,771,776,736,757,745,754,736,744,731,766,736,740,729,737,776,762,751,737,757,761,737,747,767,750,741,741]
#
#
# receive = [271,271,268,273,261,256,275,260,264,267,261,284,277,270,259,269,282,275,288,281,275,268,265,268,269,272,264,271,276,277,268,267,261,272,270,268,268,286,267,265,266,261,265,267,279,265,268,266,286,270]
#
# result = []
# for i in range(10,51,10):
#     newsend = [j * (i//2) for j in send]
#     newreceive = [j * (i//2) for j in receive]
#     temp = []
#     random.shuffle(initData)
#     random.shuffle(newsend)
#     random.shuffle(newreceive)
#     for k in range(50):
#         temp.append(initData[k]+genID[i//10-1][k]+newsend[k]+newreceive[k])
#     result.append(temp)
# print(result)


initData = [374, 394, 380, 372, 374, 374, 374, 382, 380, 374, 374, 372, 374, 372, 378, 382, 376, 384, 384, 374, 374, 372, 386, 382, 372, 380, 384, 374, 374, 382, 380, 384, 374, 376, 384, 374, 374, 374, 374, 380, 380, 386, 372, 372, 380, 374, 374, 384, 372, 374]

genID = [
    [216,216,214,214,215,219,216,214,217,217,214,214,215,215,217,216,213,213,215,219,214,215,215,219,321,216,215,217,215,216,217,218,215,216,215,216,215,218,219,216,215,216,218,295,217,215,214,218,217,216],
    [269,266,272,266,270,271,271,271,270,268,267,269,268,266,271,267,269,272,266,267,265,265,271,267,270,271,270,268,267,265,268,267,271,266,268,270,271,268,268,270,270,269,267,271,267,268,271,271,270,266],
    [330,323,324,328,325,325,329,324,328,325,396,328,330,322,330,331,328,325,324,323,325,324,324,328,323,324,402,322,330,324,324,326,328,329,329,330,326,328,330,328,324,324,324,328,324,324,332,328,324,325],
    [330,323,324,328,325,325,329,324,328,325,396,328,330,322,330,331,328,325,324,323,325,324,324,328,323,324,402,322,330,324,324,326,328,329,329,330,326,328,330,328,324,324,324,328,324,324,332,328,324,325],
    [471,465,471,464,462,471,463,462,463,470,462,461,471,473,471,463,472,472,464,471,463,464,462,464,471,462,472,462,463,463,463,472,472,470,463,474,463,465,474,471,463,461,472,473,464,472,463,463,474,473]
]

send = [177, 160, 160, 154, 182, 192, 167, 167, 155, 170, 151, 156, 160, 152, 174, 153, 161, 162, 154, 155, 164, 153, 165, 166, 169, 152, 154, 158, 153, 181, 166, 178, 170, 170, 170, 160, 173, 176, 167, 193, 165, 160, 160, 167, 164, 154, 165, 172, 166, 171]

receive = [96,116,95,91,92,91,86,94,97,101,97,97,93,105,113,118,91,98,105,97,98,106,103,98,118,100,104,95,103,102,98,103,100,101,120,102,120,103,107,101,100,100,99,94,95,95,101,103,100,95]

result = []
for i in range(10,51,10):
    newsend = [j * i for j in send]
    newreceive = [j * i for j in receive]
    temp = []
    random.shuffle(initData)
    random.shuffle(newsend)
    random.shuffle(newreceive)
    for k in range(50):
        temp.append(initData[k]+genID[i//10-1][k]+newsend[k]+newreceive[k])
    result.append(temp)
print(result)