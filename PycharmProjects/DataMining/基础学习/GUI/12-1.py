from tkinter import *

root = Tk()  # 创建一个根窗口，通过实例化，但是创建出来后立马关闭了，root是一个对象
root.title('个人所得税计算器 v1.0') #
root.geometry('800x600+350+100')
inputLabel = Label(root, text='请输入月输入:', bg='red', font='宋体 20') #实例化一个标签对对象
inputLabel.pack(padx=5,pady=50,fill=X) # 将定义好了的标签放置到界面内，可以设置位置

inputLabel = Label(root, text='请输入月输入:', bg='red', font='宋体 20') #实例化一个标签对对象
inputLabel.pack(padx=5,pady=50,fill=BOTH, expand=True) # 将定义好了的标签放置到界面内，可以设置位置

root.mainloop()  # 让上面的窗口陷入循环，等待用户操作，如鼠标点击，输入，可以理解是不停的刷新，无限循环的等待
