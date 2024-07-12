import numpy as np
from scipy.optimize import linear_sum_assignment

cost = np.array([[5, 4, 9, 7, 2], [8, 6, 7, 4, 1], [4, 9, 6, 8, 7], [5, 6, 10, 8, 4], [7, 4, 11, 8, 3]])
row_index, column_index = linear_sum_assignment(cost)
print(row_index)  # 行索引
print(column_index)  # 行索引的最优指派的列索引
print(cost[row_index, column_index])  # 每个行索引的最优指派列索引所在的元素
print(cost[row_index, column_index].sum())  # 求和

