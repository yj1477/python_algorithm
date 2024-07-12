import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

x=np.arange(-10,10,0.1)
y=np.sin(x)
plt.scatter(x,y)
plt.title("正弦波显示")
plt.show()

ma = 0
print(y) 
for i in y:
     
    if y.any() == 0: 
        ma = x
print("ma = ", ma)

