import numpy as np  
import matplotlib.pyplot as plt  
plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  #用来正常显示负号

# 生成一个包含两个正弦波的信号  
fs = 1000 # 采样率  
t = np.arange(0, 1, 1/fs) # 时间轴  
f1 = 5  # 第一个正弦波的频率  
f2 = 10 # 第二个正弦波的频率  
f3 = 15 # 随机波形的频率 
random_wave = np.random.randn(len(t)) * np.exp(1j * 2 * np.pi * f3 * t)  
a = np.sin(2*np.pi*f1*t)
b = np.sin(2*np.pi*f2*t)
c = np.fft.fft(random_wave)
signal = a + b + c
# 对信号进行傅里叶变换  
n = len(signal) # 信号长度  
k = np.arange(n) # 频率轴  
freq = k * fs / n # 计算每个频率点对应的实际频率  
y = np.fft.fft(signal) # 对信号进行傅里叶变换  
# 找到两个正弦波在频域上的位置  
idx1 = np.argmin(np.abs(freq - f1))  
idx2 = np.argmin(np.abs(freq - f2))  

# 解调出两个正弦波的时域波形  
sine1 = np.real(y[idx1] * np.exp(1j * 2 * np.pi * f1 * t))  
sine2 = np.real(y[idx2] * np.exp(1j * 2 * np.pi * f2 * t))  
sine3 = np.fft.ifft(y)
# 绘制原始信号和解调出的两个正弦波的波形图  
plt.figure(figsize=(12, 6))  
plt.subplot(3, 1, 1)  
plt.plot(t, a)  
plt.title('正弦波1')  
plt.subplot(3, 1, 2)  
plt.plot(t, b)  
plt.title('正弦波2')  
plt.subplot(3, 1, 3)  
plt.plot(t, c)  
plt.title('随机波')  
plt.tight_layout()  



plt.figure(figsize=(12, 6))
plt.plot(t, y, label='y') 
plt.title('傅里叶变换后的波形')  
plt.xlabel('Frequency (Hz)')  
plt.ylabel('Amplitude')  
plt.tight_layout()  


# 绘制解调出的两个正弦波和随机波形图  
plt.figure(figsize=(12, 6))  
plt.subplot(3, 1, 1)  
plt.plot(t, sine1)  
plt.title('正弦波1')  
plt.subplot(3, 1, 2)  
plt.plot(t, sine2)  
plt.title('正弦波2')  
plt.subplot(3, 1, 3)  
plt.plot(t, sine3)  
plt.title('随机波')  
plt.tight_layout()  
plt.show()