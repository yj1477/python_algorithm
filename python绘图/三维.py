import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义四维超立方体的所有顶点
vertices = np.array([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0],
                     [0, 0, 1, 0], [1, 0, 1, 0], [0, 1, 1, 0], [1, 1, 1, 0]])

# 创建一个3D图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制四维超立方体的边
for i in range(len(vertices)):
    for j in range(i+1, len(vertices)):
        if np.sum(np.abs(vertices[i] - vertices[j])) == 1:
            ax.plot([vertices[i][0], vertices[j][0]], [vertices[i][1], vertices[j][1]], [vertices[i][2], vertices[j][2]], 'k-', lw=1)

# 设置轴标签和限制
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(-0.5, 1.5)
ax.set_zlim(-0.5, 1.5)

# 显示图形
plt.show()
