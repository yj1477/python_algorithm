import time
import random


# 目标函数
def f(x: list) -> int:
    return x[0] ** 2 + x[1] ** 2 + 3 * x[2] ** 2 + 4 * x[3] ** 2 + 2 * x[4] ** 2 - 8 * x[0] - 2 * x[1] - 3 * x[2] - x[
        3] - 2 * x[4]


# 约束向量函数
def g(x: list) -> list:
    res=[]
    res.append(sum(x) - 400)
    res.append(x[0] + 2 * x[1] + 2 * x[2] + x[3] + 6 * x[4] - 800)
    res.append(2 * x[0] + x[1] + 6 * x[2] - 200)
    res.append(x[2] + x[3] + 5 * x[4] - 500)
    return res


random.seed(time.time)
pb = 0
xb = []
for i in range(10 ** 6):
    x = [random.randint(0, 99) for i in range(5)]  # 产生一行五列的区间[0, 99] 上的随机整数
    rf = f(x)
    rg = g(x)
    if all((a < 0 for a in rg)):  # 若 rg 中所有元素都小于 0
        if pb < rf:
            xb = x
            pb = rf
print('x1-x5的取值：', xb)
print('目标函数值：', pb)
