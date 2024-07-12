import numpy as np  
import matplotlib.pyplot as plt  
  
# 生成一个具有特定频率的随机波形  
fs = 1000  
f = 10  
t = np.arange(0, 1, 1/fs)  
random_wave = np.random.randn(len(t)) * np.exp(1j * 2 * np.pi * f * t)  
  
# 对随机波形进行傅里叶变换  
fourier_transform = np.fft.fft(random_wave)  
  
# 解调傅里叶变换后的信号  
demodulated_wave = np.fft.ifft(fourier_transform)  
  
# 绘制原始随机波形、傅里叶变换后的频谱和解调后的信号  
plt.subplot(3, 1, 1)  
plt.plot(t, random_wave)  
plt.title('Original Random Wave')  
plt.subplot(3, 1, 2)  
plt.plot(t, np.abs(fourier_transform))  
plt.title('Spectrum of Random Wave')  
plt.subplot(3, 1, 3)  
plt.plot(t, demodulated_wave)  
plt.title('Demodulated Wave')  
plt.tight_layout()  
plt.show()