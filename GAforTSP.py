import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix  # 用于计算欧式距离
import math
import random
import matplotlib.pyplot as plt

def begin_population(dt_city):  # 种群初始化
    population = []
    for i in range(count):
        population.append(np.random.permutation(dt_city))
    return population


def fit_func(dt, dt_city):  # 计算适应度函数
    d_matrix = distance_matrix(dt.values, dt.values)
    d_sum = 0
    for i in range(len(dt_city)):
        if i == len(dt_city) - 1:
            d_sum = d_sum + d_matrix[dt_city[i]][dt_city[0]]
        else:
            d_sum = d_sum + d_matrix[dt_city[i]][dt_city[i + 1]]
    return 1 / d_sum


def select(dt, pop):  # 选择
    fit = np.array([])
    for i in range(len(pop)):
        fit = np.append(fit, fit_func(dt, pop[i]))
    fit_sum = fit.sum()
    p_array = fit / fit_sum
    idx = np.random.choice(np.arange(len(pop)), size=count, p=p_array.tolist())
    new_pop = []
    for i in idx:
        new_pop.append(pop[i])
    return new_pop


# 交叉
def cross(pop, cross_rate):
    new_pop = []
    for i in pop:
        child = i
        if np.random.rand() < cross_rate:
            idx = int(np.random.choice(np.arange(len(pop)), size=1))
            j = pop[idx]
            left = np.random.randint(0, len(j) - 2)
            right = np.random.randint(left + 1, len(j) - 1)
            gene = j[left:right]
            child = i.copy()
            c_l = child[:left]
            c_m = child[left:right]
            c_r = child[right:]
            g_ = [x for x in c_m if x not in gene]
            for x in c_l:
                if x in gene:
                    c_l[c_l == x] = g_[0]
                    g_ = g_[1:]
            for x in c_r:
                if x in gene:
                    c_r[c_r == x] = g_[0]
                    g_ = g_[1:]
            child[left:right] = gene
        new_pop.append(child)
    return new_pop


# 变异
def mutation(pop, mutation_rate):
    new_pop = []
    for i in pop:
        i
        if np.random.rand() < mutation_rate:
            left = np.random.randint(0, len(i) - 2)
            right = np.random.randint(left + 1, len(i) - 1)
            mmm = i[left]
            i[left] = i[right]
            i[right] = mmm
        new_pop.append(i)
    return new_pop


if __name__ == '__main__':
    dt = pd.read_excel("data.xlsx", index_col=0)
    count = 150  # 种群数量
    cross_rate = 0.3  # 交叉概率
    mutation_rate = 0.008  # 变异概率
    T = 5000
    pop = begin_population(dt.index.values)
    for i in range(T):
        pop = select(dt, pop)
        pop = cross(pop, cross_rate)
        pop = mutation(pop, mutation_rate)


    #print(pop)
    fit = np.array([])
    for i in range(len(pop)):
        fit = np.append(fit, fit_func(dt, pop[i]))
    final = pop[fit.argmax()]
    print(1 / fit.max())
    dt_f = dt.reindex(final)
    X = dt_f['X'].tolist()
    Y = dt_f['Y'].tolist()

    plt.plot(X,Y,marker="^")
    plt.show()

