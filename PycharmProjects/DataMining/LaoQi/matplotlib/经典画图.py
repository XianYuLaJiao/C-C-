import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import math

# 数据整理
x = np.random.randn(1000)
y = x**3.222222
data = pd.DataFrame({'x': x, 'y': y})

# 新建画布，并且画上x轴与y轴
fig = plt.figure(figsize=(15, 15), dpi=100)  # 创建画布
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # 在画布上创建axes对象，即坐标系对象
ax.set_xlabel('x', fontsize=16)  # 设置x轴标签
ax.set_ylabel('y', fontsize=16)  # 设置y轴标签
ax.set_xlim(-1, 1)  # 设置x轴刻度范围
ax.set_ylim(0, 1)  # 设置y轴刻度范围
# 具体设置刻度线和刻度标签 locator是刻度线 formatter是刻度标识标签
xmajor_locator = MultipleLocator(0.1)  # 用MultipleLocator对象设置主刻度每0.1一个大刻度线
xmajor_formatter = FormatStrFormatter('%1.2f')  # 规定大刻度标签为保留两位小数的浮点数
xminor_locator = MultipleLocator(0.01)  # 规定小刻度线的间隔为0.01，即没0.01一个小刻度线

ymajor_locator = MultipleLocator(0.1)
ymajor_formatter = FormatStrFormatter('%1.1f')
yminor_locator = MultipleLocator(0.01)

ax.xaxis.set_major_locator(xmajor_locator)
ax.xaxis.set_major_formatter(xmajor_formatter)

ax.yaxis.set_major_locator(ymajor_locator)
ax.yaxis.set_major_formatter(ymajor_formatter)

ax.xaxis.set_minor_locator(xminor_locator)
ax.yaxis.set_minor_locator(yminor_locator)

ax.grid(True)  # 现栅栏线

ax.scatter(x, y, c='k',alpha=0.3 )
plt.show()