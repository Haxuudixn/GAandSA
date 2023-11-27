# GAandSA（遗传算法与退火算法实现）
***
算法实现语言：python  
引用库：  
pandas库用于引入数据、数组管理、随机数生成等  
numpy、scipy库用于数组管理、随机数生成、科学计算等  
matplotlib库用于旅行商问题图像绘制  
***
## 旅行商问题上的应用
### 问题概述及代码说明
<strong>问题设置：</strong>

假设有一个旅行商人要拜访全国31个省会城市，他需要选择所要走的路径，路径的限制是每个城市只能拜访一次，而且最后要回到原来出发的城市。对路径选择的要求是：所选路径的路程为所有路径之中的最小值。

<strong>数据导入：</strong>

dataforTSP.xlsx文件中city列代表某个城市，X、Y代表该城市的坐标值。

<strong>代码执行：</strong>

遗传算法解决旅行商问题：GAforTSP.py  
Input：count（种群数量）、cross_rate（交叉概率）、mutation_rate（变异概率）、T（迭代次数）、dt(城市坐标数据)  
Output：dt_f（最佳路线）  
退火算法解决旅行商问题：SAforTSP.py  
Input:initial_t(初始温度)、lowest_t(最低温度)、M（开始改变温度的次数）、iteration(设置迭代次数)  
Output:dt_f(最佳路线)  
***
## 函数极值问题上的应用
### 问题概述及代码说明
<strong>问题设置：</strong>


求函数y=x^3−60x^2−4x+6在(0，100)的极小值。  
<strong>代码执行：</strong>


遗传算法解决极值问题：GAforex.py  
Input：count（种群数量）、cross_rate（交叉概率）、mutation_rate（变异概率）、T（迭代次数）、function(函数)  
Output：x（最小值坐标）  ，function(x)（最小值）

退火算法解决极值问题：SAforex.py
Input：initial_t（初始温度）、lowest_t （最低温度）、M（改变温度的次数）、iteration（迭代次数）、 function(函数)  
Output：x（最小值）、  function(x)（最小值）
