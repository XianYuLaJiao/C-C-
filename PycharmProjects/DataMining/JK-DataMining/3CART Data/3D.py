import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
data = pd.read_excel(r'C:\Users\jiaojian\Desktop\data002.xlsx')
datadrop = data
x = datadrop['X轴坐标']
y = datadrop['Y轴坐标']
z = datadrop['Z轴坐标']
ax.scatter(x, y, z, c='g', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()