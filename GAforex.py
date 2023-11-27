import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix  # 用于计算欧式距离
import math
import random
import matplotlib.pyplot as plt


def function(x):
    y = x ** 3 - 60 * x ** 2 - 4 * x + 6
    return y


def begin_population(count, length):  # 种群初始化
    population = np.random.randint(0, 2, (count, length))
    return population


def bintodec(pop):  # 二进制转十进制
    pop_ = pop.copy()
    num = int(''.join(map(str, pop_)), 2)
    return num * 100 / 1023


def fit_func(popi):  # 计算适应度函数
    x = bintodec(popi)
    obj = function(x)
    return obj


def select(pop):  # 选择
    fit = np.array([])
    for i in range(len(pop)):
        fit = np.append(fit, fit_func(pop[i]))
    fit_x = fit-2*fit.min()
    fit_x = 1/fit_x
    fit_sum = fit_x.sum()
    p_array = fit_x / fit_sum
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
            child[left:right] = gene
        new_pop.append(child)
    return new_pop


# 变异
def mutation(pop, mutation_rate):
    new_pop = []
    for i in pop:
        if np.random.rand() < mutation_rate:
            x = np.random.randint(10)
            if i[x] == 1:
                i[x] = 0
            else:
                i[x] = 1
        new_pop.append(i)
    return new_pop


if __name__ == '__main__':
    count = 150  # 种群数量
    cross_rate = 0.3  # 交叉概率
    mutation_rate = 0.008  # 变异概率
    T = 5000
    length = 10
    pop = begin_population(count, length)
    for i in range(T):
        pop = select(pop)
        pop = cross(pop, cross_rate)
        pop = mutation(pop, mutation_rate)

    # print(pop)
    fit = np.array([])
    for i in range(len(pop)):
        fit = np.append(fit, fit_func(pop[i]))
    final = pop[fit.argmin()]

    X_out = bintodec(final)
    Y_out = function(X_out)
    print(X_out, Y_out)
