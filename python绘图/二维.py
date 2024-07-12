import matplotlib.pyplot as plt  
import numpy as np  
  
# 四维超立方体的16个顶点  
# 这里我们使用四维坐标 (x, y, z, w)，但我们只关心x和y进行二维投影  
vertices = [  
    (0, 0, 0, 0), (1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0),  
    (0, 0, 1, 0), (1, 0, 1, 0), (0, 1, 1, 0), (1, 1, 1, 0),  
    (0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1), (1, 1, 0, 1),  
    (0, 0, 1, 1), (1, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1)  
]  
  
# 提取x和y坐标进行二维投影  
projected_vertices = [(v[0], v[1]) for v in vertices]  
  
# 使用matplotlib绘制二维投影  
plt.figure(figsize=(8, 6))  
plt.scatter(*zip(*projected_vertices), color='blue', s=100)  # 绘制顶点  
  
# 连接顶点形成图形（这里只连接相邻的顶点以简化图形）  
for i in range(8):  
    # 连接在同一三维立方体的两个面上的顶点  
    plt.plot([projected_vertices[i][0], projected_vertices[i+8][0]],  
             [projected_vertices[i][1], projected_vertices[i+8][1]],  
             color='red', linestyle='-')  
  
    # 连接在同一三维立方体的两个相对的边上的顶点  
    if i < 4:  
        plt.plot([projected_vertices[i][0], projected_vertices[i+4][0]],  
                 [projected_vertices[i][1], projected_vertices[i+4][1]],  
                 color='green', linestyle='-')  
  
# 添加坐标轴标签和标题  
plt.xlabel('X Axis')  
plt.ylabel('Y Axis')  
plt.title('2D Projection of a 4D Hypercube (Tesseract)')  
  
# 显示图形  
plt.show()