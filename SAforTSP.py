import random
import numpy as np
import math
import pandas as pd
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt

def distance(dt, dt_city):  # 计算欧氏距离
    d_matrix = distance_matrix(dt.values, dt.values)
    d_sum = 0
    for i in range(len(dt_city)):
        if i == len(dt_city) - 1:
            d_sum = d_sum + d_matrix[dt_city[i]][dt_city[0]]
        else:
            d_sum = d_sum + d_matrix[dt_city[i]][dt_city[i + 1]]
    return d_sum


if __name__ == '__main__':
    dt = pd.read_excel("dataforTSP.xlsx", index_col=0)
    initial_t = 2000  # 初始温度
    lowest_t = 0.001  # 最低温度
    M = 150  # 当连续多次都不接受新的状态，开始改变温度
    iteration = 5000  # 设置迭代次数
    t_current = initial_t
    dt_city = np.random.permutation(dt.index.values)
    dist = distance(dt, dt_city)
    while (t_current > lowest_t):
        count_m = 0
        count_iter = 0
        while (count_m < M and count_iter < iteration):  # 内循环，连续多次不接受新的状态或者是迭代多次,跳出内循环
            i = 0
            j = 0
            while (i == j):  # 防止随机了同一城市
                i = random.randint(0, len(dt)-1)
                j = random.randint(0, len(dt)-1)
            dt_city_n = dt_city.copy()
            dt_city_n[[i, j]] = dt_city_n[[j, i]]
            dist_n = distance(dt, dt_city_n)
            d_dist = dist_n - dist
            ex_p = math.exp(-d_dist / t_current)
            rand = np.random.random()
            if d_dist < 0 or (d_dist > 0 and ex_p > rand):
                dt_city = dt_city_n
                dist = dist_n
            else:
                count_m = count_m + 1
            count_iter = count_iter + 1
        t_current = 0.99*t_current

dis_min = dist
final = dt_city
dt_f = dt.reindex(final)
X = dt_f['X'].tolist()
Y = dt_f['Y'].tolist()
print(dist)
plt.plot(X,Y,marker="^")
plt.show()