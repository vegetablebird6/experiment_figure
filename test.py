import numpy as np
import random
l = [7.73, 15.30,22.88,30.45,38.03]
res = []
for i in range(5):
    res.append(l[i] * 1.1 + (70 * (i+1)*10*3)/1000)
print(res)