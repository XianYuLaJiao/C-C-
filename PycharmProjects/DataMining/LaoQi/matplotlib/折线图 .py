from matplotlib import pyplot as plt

x = range(2,26,2)

y = [15,13,14.5,17,20,25,26,26,27,22,18,15]

plt.figure(figsize=(20,15),dpi=150) # figsize是图片尺寸大小设置，dpi是一英寸内像素点个数，代表清晰度，越高越清晰。

plt.plot(x, y) # 绘图

plt.savefig('./t1.png')  # 保存的方法，必须在绘制完后保存

plt.show() # 展示