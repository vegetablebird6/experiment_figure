# 未优化
# from math import comb
#
# def calculate_probability(x, i, S, n):
#     return comb(x-1, i-1) * comb(S-x, n-i) / comb(S, n)
#
# def maximum_guessing_probability(S, n):
#     max_probabilities = []
#     for i in range(1,n+1):
#         max_probability = 0
#         for x in range(i, S-(n-i)+1):
#             max_probability = max(calculate_probability(x, i, S, n), max_probability)
#         max_probabilities.append(max_probability)
#         print(max_probability)
#
# S = 2**11
# n = 50
#
# maximum_guessing_probability(S, n)
# ===============================================================================================
# 优化查询范围
# from math import comb,log2
#
# def calculate_probability(x, i, S, n):
#     return comb(x-1, i-1) * comb(S-x, n-i) / comb(S, n)
#
# def maximum_guessing_probability(S, n):
#     list = [2,4,7,13,25]
#     max_range = int(S / 2 ** (int(log2(n))))
#     min_range = 1
#     max_probabilities = []
#     for i in range(1,n//2+1):
#         max_probability = 0
#         for x in range(min_range, max_range+1):
#             max_probability = max(calculate_probability(x, i, S, n), max_probability)
#         print(max_probability)
#         max_probabilities.append(max_probability)
#         if i in list:
#             min_range = max_range + i
#             max_range = max_range * 2
#
# S = 2**14
# n = 50
#
# maximum_guessing_probability(S, n)
# ===============================================================================================
# 多进程查询
# from math import comb,log2,ceil
# from multiprocessing import Pool, Manager
#
# def calculate_probability(x, i, S, n):
#     return comb(x-1, i-1) * comb(S-x, n-i) / comb(S, n)
#
# def sub_task(sub_min_range, sub_max_range, i, S, n, my_list):
#     max_probability = 0
#     for x in range(sub_min_range, sub_max_range+1):
#         max_probability = max(calculate_probability(x, i, S, n), max_probability)
#     my_list.append(max_probability)
#
# def maximum_guessing_probability(S, n, i, min_range, max_range):
#     manager = Manager()
#     my_list = manager.list()
#     interval = (max_range - min_range) // 10
#     sub_min_range = min_range
#     sub_max_range = sub_min_range + interval
#     p = Pool(10)
#     for j in range(10):
#         p.apply_async(sub_task, args=(sub_min_range,sub_max_range,i, S, n, my_list,))
#         sub_min_range = sub_max_range
#         if j != 8:
#             sub_max_range = sub_min_range + interval
#         else:
#             sub_max_range = max_range
#     p.close()
#     p.join()
#     # print(my_list)
#     print(max(my_list))
#
# if __name__=='__main__':
#     S = 2 ** 29
#     n = 50
#     max_range = int(S / 2 ** (int(log2(n))))
#     min_range = 1
#     list = [2,4,7,13,25]
#     # maximum_guessing_probability(S, n, 25)
#     for i in range(1, 26):
#         if i - 1 in list:
#             min_range = max_range
#             max_range = max_range * 2
#         maximum_guessing_probability(S, n, i, min_range, max_range)

# result
# 9.313225746154785e-08
# 3.461526833339259e-08
# 2.5737055824708042e-08
# 2.1532783556302813e-08
# 1.8983534636303025e-08
# 1.7241866984387648e-08
# 1.5965003628384602e-08
# 1.498458852361369e-08
# 1.4207107602997257e-08
# 1.3575981380634252e-08
# 1.3054753051628411e-08
# 1.2618772683651448e-08
# 1.225073096151305e-08
# 1.1938100722548432e-08
# 1.1671593352175815e-08
# 1.1444187030263417e-08
# 1.1250493015197223e-08
# 1.1086330057222256e-08
# 1.0948431571427638e-08
# 1.0834240208225823e-08
# 1.0741761658911186e-08
# 1.066945975765324e-08
# 1.0616181225409169e-08
# 1.0581102392152162e-08
# 1.0563692858522121e-08