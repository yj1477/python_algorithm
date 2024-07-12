""" 非线性规划
    方法一:使用cvxpy库
    注意:还要安装cplex库"""

# import cvxpy as cp
# import numpy as np
# c1=np.array([1, 1, 3, 4, 2])
# c2=np.array([-8, -2, -3, -1, -2])
# a=np.array([[1, 1, 1, 1, 1], [1, 2, 2, 1, 6], [2, 1, 6, 0, 0], [0, 0, 1, 1, 5]])
# b=np.array([400, 800, 200, 200])
# x=cp.Variable(5,integer=True)
# obj=cp.Minimize(c1@(x**2)+c2@x)
# con=[0<=x, x<=99, a@x<=b]
# prob = cp.Problem(obj, con)
# prob.solve()
# print("最优值为:",prob.value)
# print("最优解为:",x.value)

"""方法二:使用scipy库"""
import numpy as np
from scipy.optimize import minimize

# 边界约束
b = (0.0, None)
bnds = (b, b, b)
f = lambda x: x[0] ** 2 + x[1] **2 + x[2] ** 2 + 8
cons = ({'type': 'ineq', 'fun': lambda x: x[0]**2 - x[1] + x[2]**2},
        {'type': 'ineq', 'fun': lambda x: -x[0] - x[1] - x[2]**3 + 20},
        {'type': 'eq', 'fun': lambda x: -x[0] - x[1]**2 + 2},
        {'type': 'eq', 'fun': lambda x: x[1] + 2 * x[2]**2 - 3})  # 4个约束条件,eq是=; ineq是>=
x0 = np.array([0, 0, 0])
# 计算
solution = minimize(f, x0, method='SLSQP',  bounds=bnds, constraints=cons)
x = solution.x
print('目标值: ', str(f(x)))
print('答案为:')
print('x1 = ', str(x[0]))
print('x2 = ', str(x[1]))
print('x3 = ', str(x[2]))
