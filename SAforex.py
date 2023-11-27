
import numpy as np
import math


def function(x):
    y = x ** 3 - 60 * x ** 2 - 4 * x + 6
    return y

if __name__ == '__main__':
    initial_t = 2000  # 初始温度
    lowest_t = 0.001  # 最低温度
    M = 150  # 当连续多次都不接受新的状态，开始改变温度
    iteration = 5000  # 设置迭代次数
    t_current = initial_t
    x = np.random.uniform(low=0, high=100)

    while (t_current > lowest_t):
        y = function(x)
        count_m = 0
        count_iter = 0
        x_n = x + np.random.uniform(low=-0.055, high=0.055) * t_current
        while (count_m < M and count_iter < iteration):  # 内循环，连续多次不接受新的状态或者是迭代多次,跳出内循环
            if 0 <= x_n <= 100:
                y_n = function(x_n)
                d = y_n - y
                ex_p = math.exp(-d / t_current)
                rand = np.random.random()
                if d < 0 or (d > 0 and ex_p > rand):
                    x = x_n
                else:
                    count_m = count_m + 1
            count_iter = count_iter + 1
        t_current = 0.99*t_current

dis_min = x
path_min = function(x)
print('x', dis_min)
print('最小值', path_min)