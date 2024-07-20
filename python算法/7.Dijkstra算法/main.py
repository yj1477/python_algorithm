import networkx as nx 
import numpy as np 
import matplotlib.pyplot as plt

inf = 1000 # the max number, it means there is no direct way
edge = [
    [0, inf, 5, 30, inf, inf],
    [2, 0, inf, inf, 8, inf],
    [inf, 15, 0, inf, inf, 7],
    [inf, inf, inf, 0, inf, inf],
    [inf, inf, inf, 4, 0, inf],
    [inf, inf, inf, 10, 18, 0]
]

new_edge = np.array(edge)
import networkx as nx 
import numpy as np 
import matplotlib.pyplot as plt

inf = 1000 # the max number, it means there is no direct way
edge = [
    [0, inf, 5, 30, inf, inf],
    [2, 0, inf, inf, 8, inf],
    [inf, 15, 0, inf, inf, 7],
    [inf, inf, inf, 0, inf, inf],
    [inf, inf, inf, 4, 0, inf],
    [inf, inf, inf, 10, 18, 0]
]

new_edge = np.array(edge)

# 若G是有向图
G = nx.DiGraph() # 建立一个有向图
l = len(new_edge)
for i in range(l): # 导入数据矩阵成为图
    for j in range(l):
        if new_edge[i][j] < inf: # 判断是否有边
            G.add_edge(i, j, weight = new_edge[i][j])
nx.draw(G, with_labels = True) # 绘图

p = nx.shortest_path(G) # 获得最短路径，返回的对象是一个字典
length = dict(nx.shortest_path_length(G)) # 计算最短路径长度

# print(p)
for i in range(l):
    for  keys, paths in p[i].items():
        print("node %d to node %d， length is %d, path is "%(i, keys, length[i][keys]), paths)
