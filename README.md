# GAandSA（遗传算法与退火算法实现、实例应用与复杂度分析）
***
算法实现语言：python
引用库：
pandas库用于引入数据、数组管理、随机数生成等
numpy、scipy库用于数组管理、随机数生成、科学计算等
matplotlib库用于旅行商问题图像绘制
***
## 算法实现思路
### 遗传算法的实现
### 退火算法的实现
***
## 旅行商问题上的应用
### 问题概述及代码说明
问题设置：

假设有一个旅行商人要拜访全国31个省会城市，他需要选择所要走的路径，路径的限制是每个城市只能拜访一次，而且最后要回到原来出发的城市。对路径选择的要求是：所选路径的路程为所有路径之中的最小值。

数据导入：

dataforTSP.xlsx文件中city列代表某个城市，X、Y代表该城市的坐标值。

代码执行：

遗传算法解决旅行商问题：GAforTSP.py  
_Input：count（种群数量）、cross_rate（交叉概率）、mutation_rate（变异概率）、T（迭代次数）、dt(城市坐标数据)
Output：dt_f（最佳路线）  
 
pop = begin_population(dt)#种群初始化  
    for i =1 to T do  
        pop = select(dt, pop)#选择  
        pop = cross(pop, cross_rate)#交叉  
        pop = mutation(pop, mutation_rate)#变异  
    end  
dt_f=max(fit_func(pop))#fit_func函数计算适应度，选择群体中适应度最大的个体输出_  

### 两种算法解决旅行商问题的优劣势
***
## 聚类问题上的应用
### 问题概述及代码说明
### 两种算法解决聚类问题的优劣势
***
## 两种算法复杂度受影响的可能因素