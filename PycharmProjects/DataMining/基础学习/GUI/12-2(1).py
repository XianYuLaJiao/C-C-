from tkinter import *

def tax_calc():
    inputcount = inputVar.get()
    outputtax = int(inputcount)*0.25
    outputVar.set('税后月收入：%.2f 元' % outputtax)


root = Tk()
root.title('7201部队')
root.geometry('400x400+300+250')

inputLabel = Label(root, text='7201部队', fg='red', font='微软雅黑 20')
inputLabel.pack(padx=3, pady=5)

inputVar = StringVar()
inputentry = Entry(root, textvariable = inputVar)
inputentry.pack()

inputButton = Button(root, text='kkkkkk', command = tax_calc)
inputButton.pack()

outputVar = StringVar()
outputVar.set('点击计算')
outputLabel= Label(root, textvariable=outputVar ,font='宋体 24',fg='green' )
outputLabel.pack(padx=5,pady=5)

root.mainloop()

# 默认的pack（）放置Label,Entry,Button都是按上往下排列发布的，可以用panel容器的方式把各部分先在panel容器
# 里面按想要的形式排布，然后再再root里面放置panel实现自定义的用户界面排布