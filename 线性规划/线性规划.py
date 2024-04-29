""" 线性规划
    方法一:使用pulp库"""

from pulp import *
#LpMinimize:求解最小值
#LpMaximize:求解最大值
# 1. 建立问题
prob = LpProblem("Problem", LpMaximize) 
#,其函数参数为name：
#变量名；lowBound变量下界；upBound变量上界；cat变量类型，可以为LpInteger\LpBinary\LpContinuous三者之一；
#e指明变量是否在目标函数和约束中存在，主要用来实现列生成算法。
# 2. 建立变量
x1 = LpVariable("x1", lowBound = 0 , upBound = 7)
x2 = LpVariable("x2", lowBound = 0 , upBound = 7)
x3 = LpVariable("x3", lowBound = 0 , upBound = 7)
# 3. 设置目标函数 z
prob += 2*x1 + 3*x2 -5*x3
# 4. 线性规划的约束条件
prob += 2*x1 - 5*x2 + x3 >= 10.0, "constraint1"
prob += x1 + 3*x2 + x3 <= 12.0,   "constraint2"
prob += x1 + x2 + x3 == 7.0, "constraint3"
# 5. 求解
prob.solve()
# 6. 打印求解状态
print("Status:", LpStatus[prob.status])
# 7. 打印出每个变量的最优值
for v in prob.variables():
    print(v.name, "=", v.varValue)
# 8. 打印最优解的目标函数值
print("z= ", value(prob.objective))